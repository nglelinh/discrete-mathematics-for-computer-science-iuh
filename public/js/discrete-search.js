// Simple Search Functionality for Discrete Mathematics Course
class DiscreteSearch {
    constructor() {
        this.searchData = [
            { title: "Logic Mệnh đề", chapter: "Chương 1", url: "/contents/chapter01/", keywords: ["logic", "mệnh đề", "chân trị"] },
            { title: "Phép toán Logic", chapter: "Chương 1", url: "/contents/chapter01/", keywords: ["AND", "OR", "NOT", "implies"] },
            { title: "Chứng minh Trực tiếp", chapter: "Chương 3", url: "/contents/chapter03/", keywords: ["chứng minh", "direct proof"] },
            { title: "Chứng minh Phản chứng", chapter: "Chương 3", url: "/contents/chapter03/", keywords: ["phản chứng", "contradiction"] },
            { title: "Quy nạp Toán học", chapter: "Chương 3", url: "/contents/chapter03/", keywords: ["quy nạp", "induction"] },
            { title: "Tập hợp", chapter: "Chương 4", url: "/contents/chapter04/", keywords: ["tập hợp", "set", "element"] },
            { title: "Phép toán Tập hợp", chapter: "Chương 4", url: "/contents/chapter04/", keywords: ["hợp", "giao", "union", "intersection"] },
            { title: "Quan hệ", chapter: "Chương 5", url: "/contents/chapter05/", keywords: ["quan hệ", "relation", "matrix"] }
        ];
        this.init();
    }

    init() {
        this.createSearchUI();
        this.bindEvents();
    }

    createSearchUI() {
        const searchHTML = `
            <div id="search-container" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999;">
                <div style="position: absolute; top: 20%; left: 50%; transform: translateX(-50%); width: 90%; max-width: 500px; background: white; border-radius: 8px; padding: 20px;">
                    <input type="text" id="search-input" placeholder="Tìm kiếm..." style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; margin-bottom: 15px;">
                    <div id="search-results" style="max-height: 300px; overflow-y: auto;"></div>
                    <button onclick="discreteSearch.close()" style="position: absolute; top: 10px; right: 15px; background: none; border: none; font-size: 20px; cursor: pointer;">×</button>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', searchHTML);
    }

    bindEvents() {
        // Ctrl+K to open search
        document.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                this.open();
            }
            if (e.key === 'Escape') this.close();
        });

        // Search input
        document.getElementById('search-input').addEventListener('input', (e) => {
            this.search(e.target.value);
        });

        // Add search button to sidebar
        const sidebar = document.querySelector('.sidebar-nav');
        if (sidebar) {
            const searchBtn = document.createElement('a');
            searchBtn.className = 'sidebar-nav-item';
            searchBtn.innerHTML = '🔍 Tìm kiếm (Ctrl+K)';
            searchBtn.style.cursor = 'pointer';
            searchBtn.onclick = () => this.open();
            sidebar.insertBefore(searchBtn, sidebar.children[1]);
        }
    }

    open() {
        document.getElementById('search-container').style.display = 'block';
        document.getElementById('search-input').focus();
    }

    close() {
        document.getElementById('search-container').style.display = 'none';
        document.getElementById('search-input').value = '';
        document.getElementById('search-results').innerHTML = '';
    }

    search(query) {
        const results = document.getElementById('search-results');
        if (!query.trim()) {
            results.innerHTML = '<p style="color: #666; text-align: center;">Nhập từ khóa để tìm kiếm</p>';
            return;
        }

        const matches = this.searchData.filter(item => 
            item.title.toLowerCase().includes(query.toLowerCase()) ||
            item.keywords.some(k => k.toLowerCase().includes(query.toLowerCase()))
        );

        if (matches.length === 0) {
            results.innerHTML = '<p style="color: #666; text-align: center;">Không tìm thấy kết quả</p>';
            return;
        }

        results.innerHTML = matches.map(item => `
            <div style="padding: 10px; border-bottom: 1px solid #eee; cursor: pointer;" onclick="window.location.href='${item.url}'; discreteSearch.close();">
                <strong style="color: #007bff;">${item.title}</strong>
                <div style="font-size: 12px; color: #666;">${item.chapter}</div>
            </div>
        `).join('');
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    window.discreteSearch = new DiscreteSearch();
});
