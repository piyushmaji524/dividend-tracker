let allDividends = [];
let sortDirection = {};
let currentSectorFilter = 'all';

// Initialize visitor counter
function initializeVisitorCounter() {
    let visitCount = localStorage.getItem('dividendTrackerVisitors');
    if (visitCount === null) {
        visitCount = 1;
    } else {
        visitCount = parseInt(visitCount) + 1;
    }
    localStorage.setItem('dividendTrackerVisitors', visitCount);
    document.getElementById('visitCount').textContent = visitCount.toLocaleString();
}

// Fetch dividends on page load
document.addEventListener('DOMContentLoaded', function() {
    initializeVisitorCounter();
    fetchDividends();
    
    // Refresh button
    document.getElementById('refreshBtn').addEventListener('click', function() {
        this.disabled = true;
        fetchDividends();
        setTimeout(() => { this.disabled = false; }, 5000);
    });
    
    // Share button
    document.getElementById('shareBtn').addEventListener('click', generateShareableCard);
    
    // Search functionality
    document.getElementById('searchInput').addEventListener('input', filterTable);
    document.getElementById('searchClear').addEventListener('click', function() {
        document.getElementById('searchInput').value = '';
        filterTable();
    });
    
    // Sector filter buttons
    document.querySelectorAll('.sector-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.sector-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            currentSectorFilter = this.dataset.sector;
            filterTable();
        });
    });
    
    // Modal functionality
    const infoModal = document.getElementById('infoModal');
    const shareModal = document.getElementById('shareModal');
    const closeButtons = document.querySelectorAll('.close');
    
    closeButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            this.closest('.modal').style.display = 'none';
        });
    });
    
    window.addEventListener('click', function(event) {
        if (event.target === infoModal) {
            infoModal.style.display = 'none';
        }
        if (event.target === shareModal) {
            shareModal.style.display = 'none';
        }
    });
    
    // Download card button
    document.getElementById('downloadCardBtn').addEventListener('click', downloadCard);
    document.getElementById('copyCardBtn').addEventListener('click', copyCardToClipboard);
});

async function fetchDividends() {
    const loading = document.getElementById('loading');
    const content = document.getElementById('content');
    
    loading.style.display = 'flex';
    content.style.display = 'none';
    
    try {
        const response = await fetch('/api/dividends');
        const data = await response.json();
        
        allDividends = data.dividends;
        
        // Update last update time
        if (data.last_update) {
            const lastUpdate = new Date(data.last_update);
            document.getElementById('lastUpdate').textContent = 
                `Last updated: ${lastUpdate.toLocaleTimeString()}`;
        }
        
        // Update count
        document.getElementById('totalCount').textContent = data.total_count;
        
        // Populate table
        populateTable(allDividends);
        
        loading.style.display = 'none';
        content.style.display = 'block';
        
    } catch (error) {
        console.error('Error fetching dividends:', error);
        loading.innerHTML = '<p style="color: red;">Error loading dividends. Please try refreshing.</p>';
    }
}

function populateTable(dividends) {
    const tbody = document.getElementById('tableBody');
    const noResults = document.getElementById('noResults');
    
    if (dividends.length === 0) {
        tbody.innerHTML = '';
        noResults.style.display = 'block';
        return;
    }
    
    noResults.style.display = 'none';
    tbody.innerHTML = dividends.map((div, index) => {
        const exDate = new Date(div.ex_dividend_date);
        const recordDate = new Date(div.record_date);
        const distributionDate = new Date(div.distribution_date);
        
        const formattedExDate = exDate.toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'short', 
            day: 'numeric' 
        });
        
        const formattedRecordDate = recordDate.toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'short', 
            day: 'numeric' 
        });
        
        const formattedDistributionDate = distributionDate.toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'short', 
            day: 'numeric' 
        });
        
        let daysBadgeClass = 'days-4plus';
        if (div.days_until_ex_date === 0) daysBadgeClass = 'days-1';
        else if (div.days_until_ex_date === 1) daysBadgeClass = 'days-2to3';
        
        let yieldClass = 'yield-neutral';
        if (div.dividend_yield > 3) yieldClass = 'yield-positive';
        
        // Eligibility status
        let eligibilityBadge = '';
        if (div.eligible_if_buy_today) {
            eligibilityBadge = '<span class="eligibility-badge eligible">✓ QUALIFIED</span>';
        } else {
            eligibilityBadge = '<span class="eligibility-badge not-eligible">✗ NOT QUALIFIED</span>';
        }
        
        return `
            <tr style="cursor: pointer;" onclick="showCompanyInfo('${div.symbol}')">
                <td class="symbol-cell">${div.symbol}</td>
                <td>${div.company_name || 'N/A'}</td>
                <td><small>${formattedExDate}</small></td>
                <td><small>${formattedRecordDate}</small></td>
                <td><small><strong>${formattedDistributionDate}</strong></small></td>
                <td>₹${div.dividend_amount.toFixed(2)}</td>
                <td>₹${div.current_price.toFixed(2)}</td>
                <td class="${yieldClass}">${div.dividend_yield.toFixed(2)}%</td>
                <td>${eligibilityBadge}</td>
            </tr>
        `;
    }).join('');
}

function filterTable() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    
    let filtered = allDividends.filter(div => {
        const matchesSearch = div.symbol.toLowerCase().includes(searchTerm) ||
                             (div.company_name && div.company_name.toLowerCase().includes(searchTerm));
        const matchesSector = currentSectorFilter === 'all' || div.sector === currentSectorFilter;
        return matchesSearch && matchesSector;
    });
    
    populateTable(filtered);
}

function sortTable(columnIndex) {
    const columnHeaders = ['symbol', 'company_name', 'dividend_date', 'days_until', 'dividend_amount', 'current_price', 'dividend_yield'];
    const columnName = columnHeaders[columnIndex];
    
    if (!sortDirection[columnIndex]) {
        sortDirection[columnIndex] = 'asc';
    } else {
        sortDirection[columnIndex] = sortDirection[columnIndex] === 'asc' ? 'desc' : 'asc';
    }
    
    allDividends.sort((a, b) => {
        let aVal = a[columnName];
        let bVal = b[columnName];
        
        // Handle numeric values
        if (typeof aVal === 'number' && typeof bVal === 'number') {
            return sortDirection[columnIndex] === 'asc' ? aVal - bVal : bVal - aVal;
        }
        
        // Handle string values
        aVal = String(aVal).toLowerCase();
        bVal = String(bVal).toLowerCase();
        
        if (sortDirection[columnIndex] === 'asc') {
            return aVal.localeCompare(bVal);
        } else {
            return bVal.localeCompare(aVal);
        }
    });
    
    populateTable(allDividends);
}

function showCompanyInfo(symbol) {
    const div = allDividends.find(d => d.symbol === symbol);
    
    if (!div) {
        alert('Company data not found!');
        return;
    }
    
    const modal = document.getElementById('infoModal');
    const modalBody = document.getElementById('modalBody');
    
    const high52w = div.high_52w ? `₹${div.high_52w.toFixed(2)}` : 'N/A';
    const low52w = div.low_52w ? `₹${div.low_52w.toFixed(2)}` : 'N/A';
    
    modalBody.innerHTML = `
        <div class="company-info">
            <div class="company-header">
                <div class="company-title">
                    <h2>${div.company_name}</h2>
                    <p style="margin: 5px 0; color: #666;">${div.description}</p>
                </div>
                <div class="company-symbol">${div.symbol}</div>
            </div>
            
            <div class="info-grid">
                <div class="info-item">
                    <label>Current Price</label>
                    <value>₹${div.current_price.toFixed(2)}</value>
                </div>
                <div class="info-item">
                    <label>Dividend Yield</label>
                    <value style="color: #2e7d32;">${div.dividend_yield}%</value>
                </div>
                <div class="info-item">
                    <label>52-Week High</label>
                    <value>${high52w}</value>
                </div>
                <div class="info-item">
                    <label>52-Week Low</label>
                    <value>${low52w}</value>
                </div>
                <div class="info-item">
                    <label>Market Cap</label>
                    <value>${div.market_cap}</value>
                </div>
                <div class="info-item">
                    <label>PE Ratio</label>
                    <value>${div.pe_ratio}</value>
                </div>
                <div class="info-item">
                    <label>Sector</label>
                    <value>${div.sector}</value>
                </div>
                <div class="info-item">
                    <label>Ex-Dividend Date</label>
                    <value>${new Date(div.ex_dividend_date).toLocaleDateString()}</value>
                </div>
            </div>
            
            <div class="roi-section">
                <h3>💰 Expected Returns</h3>
                <div class="roi-grid">
                    <div class="roi-card">
                        <div class="value">${div.annual_dividend.toFixed(2)}</div>
                        <div class="label">Annual Dividend (₹ per share)</div>
                    </div>
                    <div class="roi-card">
                        <div class="value">${div.roi_1year.toFixed(2)}%</div>
                        <div class="label">1-Year ROI</div>
                    </div>
                    <div class="roi-card">
                        <div class="value">₹${div.five_year_dividend.toFixed(2)}</div>
                        <div class="label">5-Year Dividend</div>
                    </div>
                    <div class="roi-card">
                        <div class="value">${div.roi_5year.toFixed(2)}%</div>
                        <div class="label">5-Year ROI</div>
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 20px; padding-top: 20px; border-top: 2px solid #e0e0e0;">
                <h3>Eligibility Status</h3>
                <p><strong>If you buy today:</strong> ${div.eligibility_status}</p>
                <p style="font-size: 0.9em; color: #666;">Ex-Dividend Date: ${new Date(div.ex_dividend_date).toLocaleDateString()}</p>
            </div>
        </div>
    `;
    
    modal.style.display = 'block';
}

async function generateShareableCard() {
    const shareBtn = document.getElementById('shareBtn');
    const shareModal = document.getElementById('shareModal');
    
    shareBtn.disabled = true;
    shareBtn.textContent = '⏳ Generating...';
    
    try {
        const response = await fetch('/api/generate-card');
        const data = await response.json();
        
        if (data.status === 'success') {
            document.getElementById('cardImage').src = data.image;
            shareModal.style.display = 'block';
        } else {
            alert('Error generating card: ' + data.message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to generate shareable card');
    } finally {
        shareBtn.disabled = false;
        shareBtn.textContent = '📱 Share Card';
    }
}

function downloadCard() {
    // Create a temporary link and trigger download
    const link = document.createElement('a');
    link.href = '/api/download-card';
    link.download = `dividend_tracker_${new Date().toISOString().split('T')[0]}.png`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function copyCardToClipboard() {
    const cardImage = document.getElementById('cardImage');
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const img = new Image();
    
    img.onload = function() {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        
        canvas.toBlob(blob => {
            const item = new ClipboardItem({ 'image/png': blob });
            navigator.clipboard.write([item]).then(() => {
                alert('✅ Image copied to clipboard! Now paste it on WhatsApp/Instagram');
            }).catch(err => {
                alert('Copy to clipboard feature not supported in this browser');
            });
        });
    };
    
    img.src = cardImage.src;
}
