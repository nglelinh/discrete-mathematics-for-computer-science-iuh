// Quét contents/**/_posts/*.md tìm data-demo="..." và ghi _data/tools.yml cho trang tools.html.
// Chạy:  node gen-tools-data.mjs   (từ thư mục explainers/)
import { readdirSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const EXPLAINERS = {
  'graph-explainer': ['🕸️', 'Đồ thị: BFS · DFS · Dijkstra', 'Vẽ/sửa đồ thị, chạy thuật toán từng bước với giả mã được tô sáng.'],
  'boolean-explainer': ['🔌', 'Đại số Boolean: K-map, Quine–McCluskey, mạch', 'Bảng chân trị, SOP/POS, don’t-care, sơ đồ mạch từ biểu thức và so sánh hai biểu thức.'],
  'pascal-explainer': ['🔺', 'Tam giác Pascal: cộng từ đỉnh xuống', 'Hoạt ảnh mỗi ô = tổng hai ô cha, tổng hàng 2ⁿ, đối xứng, cây gậy khúc côn cầu, tô màu mod 2.'],
  'qm-explainer': ['🧮', 'Quine–McCluskey từng bước', 'Dán cột, nguyên nhân nguyên tố, bảng phủ, cốt yếu, trội hàng/cột, Petrick; 2–6 biến, don’t-care, đối chiếu K-map.'],
  'venn-explainer': ['⭕', 'Tập hợp: biểu đồ Venn', 'Tô vùng theo biểu thức, so sánh hai biểu thức, bao hàm–loại trừ.'],
  'relation-explainer': ['🔗', 'Quan hệ: tính chất, bao đóng, Hasse', 'Phản ví dụ cho từng tính chất, Warshall từng bước, lớp tương đương, sơ đồ Hasse.'],
  'function-explainer': ['ƒ', 'Hàm số: đơn/toàn/song ánh', 'Sửa mũi tên giữa hai tập, hàm ngược và hàm hợp.'],
  'counting-explainer': ['🔢', 'Đếm: Pascal, tổ hợp, chuồng bồ câu', 'Tam giác Pascal, liệt kê tổ hợp/hoán vị, sao–thanh chắn, chuồng bồ câu.'],
  'recurrence-explainer': ['🔁', 'Hệ thức truy hồi & chia để trị', 'Công thức đóng từ đa thức đặc trưng, nghiệm riêng, định lý Master, cây đệ quy.'],
  'automata-explainer': ['🤖', 'Otomat: DFA · NFA · tập con · tối thiểu hóa', 'Mô phỏng từng ký tự, xây dựng tập con NFA→DFA, tối thiểu hóa DFA, tự vẽ máy.'],
  'tree-explainer': ['🌳', 'Cây: Huffman, duyệt cây, BST', 'Gộp Huffman từng bước, bốn kiểu duyệt cây, chèn/tìm/xóa trong BST.'],
  'exprtree-explainer': ['🌿', 'Cây biểu thức Boolean', 'Gõ công thức logic, xem cây cú pháp, đổi giá trị biến và tính từ lá lên gốc; chỉ ra liên kết chính.'],
  'topo-explainer': ['📋', 'Sắp xếp topo: Kahn và DFS', 'Bậc vào, hàng đợi, ngăn xếp đệ quy, hậu tự đảo; phát hiện chu trình khi thêm cạnh ngược.'],
  'induction-explainer': ['🁢', 'Quy nạp: hiệu ứng domino', 'Cơ sở + bước quy nạp làm domino đổ; ví dụ thiếu cơ sở và phản ví dụ n² + n + 41 tại n = 40.'],
  'dpll-explainer': ['🧩', 'SAT solver DPLL từng bước', 'Lan truyền đơn vị, quyết định, quay lui trên CNF tùy ý; ví dụ chuồng bồ câu 3→2 vô nghiệm.'],
  'bits-explainer': ['🔢', 'Nhị phân: bù hai, cộng, endianness, Y2038', 'Bấm bit để đọc giá trị bù hai, lấy số đối, cộng có nhớ và tràn số, thứ tự byte, tràn Unix time.'],
  'cyk-explainer': ['🔺', 'CYK: bảng phân tích', 'Điền bảng CYK từng điểm chia cho văn phạm dạng chuẩn Chomsky; tự sửa văn phạm và chuỗi.'],
  'derive-explainer': ['🌲', 'Dẫn xuất trái nhất và cây phân tích', 'Cây hiện dần theo dẫn xuất; so sánh nhiều cây của văn phạm nhập nhằng (biểu thức, dangling else).'],
  'pda-explainer': ['📚', 'Otomat đẩy xuống (PDA)', 'Chuỗi vào, trạng thái và ngăn xếp đổi theo từng chuyển tiếp; aⁿbⁿ, wwᴿ không tất định, ngoặc cân bằng.'],
  'tm-explainer': ['📼', 'Máy Turing từng bước', 'Băng, đầu đọc, bảng chuyển; cộng 1 nhị phân, nhận dạng 0ⁿ1ⁿ, cộng đơn phân.'],
  'numtheory-explainer': ['🔐', 'Lý thuyết số: Euclid, modulo, RSA', 'Euclid mở rộng/Bézout, mặt đồng hồ modulo, lũy thừa nhanh, sàng, RSA đồ chơi.'],
  'infinity-explainer': ['♾️', 'Vô hạn: đường chéo Cantor, khách sạn Hilbert', 'Lật đường chéo để tạo dãy không có trong danh sách, khách sạn vô hạn nhận thêm khách, hàm ghép cặp Cantor ℕ×ℕ → ℕ.'],
  'adder-explainer': ['➕', 'Bộ cộng ripple-carry', 'Chuỗi bộ cộng toàn phần 4 bit, nhớ lan từng tầng, cộng/trừ bù hai, tràn số và độ trễ cổng.'],
  'sim-explainer': ['🎲', 'Mô phỏng xác suất: sinh nhật, băm, hàng đợi', 'Nghịch lý sinh nhật, va chạm bảng băm, hàng đợi nhiều máy phục vụ và định luật Little.'],
  'inference-explainer': ['⚖️', 'Kiểm tra suy diễn', 'Nhập tiền đề và kết luận, bảng chân trị tìm phản ví dụ; modus ponens/tollens, tam đoạn luận, nguỵ biện khẳng định hậu kiện.'],
  'match-explainer': ['🔀', 'Ghép cặp và tô màu đồ thị', 'Đường tăng Kuhn từng bước, điều kiện Hall; tô màu tham lam theo thứ tự đỉnh so với số màu tối ưu.'],
  'reduction-explainer': ['🔁', 'Quy dẫn NP: SAT→3SAT, IS/Clique/VC, xấp xỉ VC', 'Tách mệnh đề thành 3-literal, tập độc lập ↔ clique ↔ phủ đỉnh, thuật toán xấp xỉ gấp đôi.'],
  'regex-explainer': ['🧵', 'Regex ↔ otomat: Thompson, loại trạng thái', 'Dựng ε-NFA Thompson từng khối, và loại trạng thái từng bước để lấy regex từ otomat.'],
  'mealy-explainer': ['⇄', 'Máy Mealy và Moore', 'Máy trạng thái có đầu ra: đầu ra theo chuyển tiếp (Mealy) hoặc theo trạng thái (Moore).'],
  'pumping-explainer': ['🎈', 'Trò chơi bổ đề bơm', 'Duyệt mọi cách chia xyz hoặc uvxyz và bơm để chứng minh ngôn ngữ không chính quy / không phi ngữ cảnh.'],
  'cfgpda-explainer': ['🔄', 'CFG → PDA', 'Ngăn xếp mô phỏng dẫn xuất trái nhất: thay biến bằng vế phải, khớp ký hiệu kết thúc.'],
  'crypto-explainer': ['🔑', 'CRT, Miller–Rabin, Diffie–Hellman', 'Giải hệ đồng dư Trung Hoa, kiểm tra nguyên tố xác suất với nhân chứng, trao đổi khóa và Eve dò logarit.'],
  'rule-explainer': ['🌿', 'Cây quy tắc cộng và nhân', 'Tính số cách từ lá lên gốc; cẩn thận khi các trường hợp giao nhau.'],
  'sort-explainer': ['📊', 'Sắp xếp và tìm kiếm', 'Bubble/insertion/selection, tuần tự và nhị phân với bộ đếm so sánh.'],
  'contradiction-explainer': ['⊥', 'Phản chứng từng bước', 'Chứng minh √2 vô tỷ và vô hạn số nguyên tố theo từng dòng, tô sáng chỗ mâu thuẫn, thử số liệu.'],
  'predproof-explainer': ['∀∃', 'Suy luận vị từ từng dòng', 'UI/UG/EI/EG với điều kiện của mỗi quy tắc, hai lỗi kinh điển và phản ví dụ trên mô hình hữu hạn.']
};
const human = (id) => id.replace(/-/g, ' ').replace(/^./, (c) => c.toUpperCase());

const found = {}; // id -> Set(path)
const titleOf = {};
for (const ch of readdirSync(join(root, 'contents')).filter((d) => d.startsWith('chapter')).sort()) {
  const dir = join(root, 'contents', ch, '_posts');
  let files = [];
  try { files = readdirSync(dir).filter((f) => f.endsWith('.md')).sort(); } catch { continue; }
  for (const f of files) {
    const path = `contents/${ch}/_posts/${f}`;
    const src = readFileSync(join(root, path), 'utf8');
    for (const m of src.matchAll(/data-demo="([^"]+)"/g)) (found[m[1]] ||= new Set()).add(path);
  }
}
const q = (s) => JSON.stringify(s);
let out = '# Tệp sinh tự động bởi explainers/gen-tools-data.mjs — đừng sửa tay.\nexplainers:\n';
for (const [id, [icon, name, desc]] of Object.entries(EXPLAINERS)) {
  out += `  - id: ${id}\n    icon: ${q(icon)}\n    name: ${q(name)}\n    desc: ${q(desc)}\n    lessons:\n`;
  for (const p of [...(found[id] || [])]) out += `      - ${q(p)}\n`;
}
out += 'widgets:\n';
for (const [id, set] of Object.entries(found).filter(([id]) => !EXPLAINERS[id]).sort()) {
  out += `  - id: ${id}\n    name: ${q(human(id))}\n    lessons:\n`;
  for (const p of set) out += `      - ${q(p)}\n`;
}
mkdirSync(join(root, '_data'), { recursive: true });
writeFileSync(join(root, '_data', 'tools.yml'), out);
console.log('explainers:', Object.keys(EXPLAINERS).length, ' widgets:', Object.keys(found).filter((i) => !EXPLAINERS[i]).length);
