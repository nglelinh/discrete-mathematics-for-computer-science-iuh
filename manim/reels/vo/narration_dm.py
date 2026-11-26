"""Lời dẫn tiếng Việt cho các reel toán rời rạc (viết theo cách đọc). REELS[tên] = (file, Scene, video, [(giây bắt đầu, lời dẫn)]).
Mốc giây lấy từ vo/probe.py (khớp thời lượng video công khai). Giọng: ElevenLabs Trường (U0vnF55XGy05G83azOfJ, eleven_v3); khi hết credit dùng Gemini Algenib."""

REELS = {
    'handshake': ('handshake.py', 'Handshake', 'handshake-lemma.mp4', [
        (0.4, 'Định lý bắt tay. Mỗi cạnh có hai đầu, nên khi cộng bậc các đỉnh, mỗi cạnh được tính hai lần. Thêm từng cạnh, tổng bậc tăng thêm hai.'),
        (11.9, 'Tổng bậc bằng hai lần số cạnh, nên số đỉnh bậc lẻ luôn là số chẵn. Ba đỉnh cùng bậc ba cho tổng chín, là số lẻ, nên không có.'),
    ]),
    'konigsberg': ('konigsberg.py', 'Konigsberg', 'konigsberg-bridges.mp4', [
        (0.4, 'Có đường đi qua cả bảy cây cầu, mỗi cầu đúng một lần không? Ta chỉ giữ lại kết nối, rồi đếm bậc mỗi đỉnh: cả bốn đỉnh đều có bậc lẻ.'),
        (10.4, 'Thử một lộ trình, nhưng đi mãi vẫn kẹt, còn một cầu chưa đi.'),
        (18.1, 'Định lý Euler: có chu trình khi mọi bậc chẵn. Ở đây có bốn đỉnh lẻ, nên không thể.'),
    ]),
    'derangement': ('derangement.py', 'Derangement', 'derangement-one-over-e.mp4', [
        (0.4, 'Hoán vị không điểm cố định: phần tử nào đứng đúng chỗ thì tô đỏ. Ta tìm những hoán vị không có số đỏ nào.'),
        (8.1, 'Xem tỉ lệ đê en chia en giai thừa khi en lớn dần: nó tiến rất nhanh về một giá trị cố định.'),
        (17.85, 'Khoảng ba mươi sáu phẩy tám phần trăm, tức một chia e.'),
    ]),
    'euclid': ('euclid.py', 'Euclid', 'euclid-gcd-tiling.mp4', [
        (0.4, 'Lát hình chữ nhật hai trăm năm mươi hai nhân một trăm linh năm bằng hình vuông lớn nhất. Dư bốn mươi hai, lát tiếp bằng hình vuông nhỏ hơn, cứ thế đến khi hết dư.'),
        (13.6, 'Cạnh hình vuông cuối cùng, hai mươi mốt, chính là ước chung lớn nhất của hai số.'),
    ]),
    'modular-cardioid': ('cardioid.py', 'Cardioid', 'modular-times-table.mp4', [
        (0.4, 'Bảng cửu chương theo modulo một trăm: nối điểm i với điểm ca nhân i. Với ca bằng hai, ta được một hình trái tim.'),
        (9.55, 'Tăng ca lên ba, bốn, năm: hình dạng đổi theo, và có thêm một điểm nhọn mỗi lần tăng.'),
        (18.3, 'Quy luật: với ca nhân, hình có ca trừ một điểm nhọn. Cứ tăng ca là thêm một cánh.'),
    ]),
    'pigeonhole-square': ('pigeonhole.py', 'Pigeonhole', 'pigeonhole-square.mp4', [
        (0.4, 'Nguyên lý chuồng chim. Chia hình vuông thành bốn ô, rồi đặt năm điểm bất kỳ vào. Thử cách đặt nào cũng vậy, năm điểm mà chỉ có bốn ô.'),
        (11.95, 'Luôn có hai điểm rơi vào cùng một ô. Hình vuông cạnh hai, mỗi ô cạnh một, nên hai điểm đó cách nhau không quá căn hai.'),
    ]),
}
