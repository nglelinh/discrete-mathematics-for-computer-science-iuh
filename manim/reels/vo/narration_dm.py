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


REELS['induction-dominoes'] = ('induction.py', 'Induction', 'induction-dominoes.mp4', [
    (0.4, 'Quy nạp toán học: chứng minh cho mọi en.'),
    (5.1, 'Một cộng hai cộng đến en bằng en nhân en cộng một, chia hai. Thử đến một nghìn vẫn đúng, nhưng en có vô hạn giá trị.'),
    (17.15, 'Hình ảnh domino. Cần hai điều. Một, viên số một đổ: đó là bước cơ sở. Hai, viên ca đổ thì kéo viên ca cộng một đổ, với mọi ca: đó là bước quy nạp. Có đủ hai điều, mọi viên đều đổ. Thiếu một, không ai đẩy viên đầu. Thiếu hai ở một chỗ, chuỗi bị đứt, các viên sau vẫn đứng.'),
    (49.2, 'Nguyên lý quy nạp. Pê của ca là giả thiết quy nạp. Ca là số bất kỳ, ta không chứng minh nó, chỉ giả sử để suy ra pê của ca cộng một.'),
    (63.05, 'Ghép hai tam giác bậc thang thành hình chữ nhật bốn nhân năm bằng hai mươi, nên tổng một đến bốn là mười. Tổng quát: hai lần tổng bằng en nhân en cộng một.'),
    (78.8, 'Chứng minh bằng quy nạp. Cơ sở: en bằng một, hai vế đều bằng một. Quy nạp: giả sử đúng với ca. Thêm số hạng ca cộng một, dùng giả thiết, rồi đặt ca cộng một ra ngoài, ta được ca cộng một nhân ca cộng hai, chia hai. Vậy đúng với mọi en từ một.'),
    (109.75, 'Thử nhiều giá trị chưa phải chứng minh. En bình phương cộng en cộng bốn mươi mốt là nguyên tố bốn mươi lần liền, nhưng en bằng bốn mươi thì không.'),
    (123.8, 'Chứng minh sai thứ nhất, quên bước cơ sở. Cho rằng en bình phương cộng en là số lẻ. Bước quy nạp nghe hoàn toàn đúng, nhưng en bằng một cho hai, là số chẵn. Thật ra tích hai số liên tiếp luôn chẵn.'),
    (144.95, 'Chứng minh sai thứ hai: mọi con ngựa cùng màu. Bỏ con cuối, bỏ con đầu, hai nhóm có phần chung nên cả đàn cùng màu. Nhưng từ một con sang hai con, hai nhóm không có con chung. Bước quy nạp phải đúng với mọi ca.'),
    (168.8, 'Quy nạp mạnh. Muốn chứng minh sáu mươi là tích các số nguyên tố, ta tách thành sáu nhân mười. Hai số này nhỏ hơn sáu mươi nhưng không phải năm mươi chín, nên cần giả thiết cho mọi số nhỏ hơn.'),
    (188.85, 'Khuôn trình bày: cơ sở, giả thiết, bước quy nạp, kết luận. Sai một bước là cả chứng minh sụp đổ.'),
])


REELS['bfs-vs-dfs'] = ('bfs_dfs.py', 'BfsDfs', 'bfs-vs-dfs.mp4', [
    (0.4, 'Duyệt đồ thị: cùng một đồ thị, hai cách đi, hàng đợi và ngăn xếp.'),
    (7.5, 'BFS duyệt theo bề rộng. Bắt đầu từ a, ta thăm từng lớp một: khoảng cách không, rồi một, rồi hai, rồi ba. Số vàng là số cạnh ít nhất từ a. Cạnh nối xê với e không thuộc cây, vì e đã được bê thêm vào trước.'),
    (36.35, 'Cây BFS cho đường đi ngắn nhất. Muốn đi từ a đến giê, ta lần ngược theo cha: a, bê, đê, giê, ba cạnh, đúng bằng khoảng cách. Vì BFS xong hết một lớp mới sang lớp sau. Chỉ đúng khi các cạnh cùng trọng số, có trọng số thì dùng Dijkstra.'),
    (58.4, 'DFS đi sâu nhất có thể, hết đường thì quay lui. Thứ tự DFS là a, bê, đê, giê, e, xê, ép, khác với thứ tự BFS. Đến xê, đỉnh a đã thăm mà không phải cha của xê, nên đó là cạnh ngược.'),
    (84.65, 'Cạnh ngược cho ta chu trình a, bê, e, xê, a. Đồ thị vô hướng có chu trình khi và chỉ khi DFS gặp cạnh ngược. Không có thì đồ thị là rừng.'),
    (101.5, 'Trong code chỉ khác một dòng. Lấy đỉnh vào sớm nhất, tức hàng đợi, là BFS. Đổi thành lấy đỉnh vào muộn nhất, tức ngăn xếp, ta luôn đi tiếp từ đỉnh mới nhất: đó là DFS. Thứ tự hơi khác bản đệ quy, nhưng vẫn là DFS hợp lệ.'),
    (124.75, 'Đặt cạnh nhau. BFS tỏa ra theo lớp, DFS lao thẳng xuống sâu. Cả hai đều có độ phức tạp ô của vê cộng e: mỗi đỉnh vào một lần, mỗi cạnh được xét hai lần.'),
    (148.0, 'Đếm thành phần liên thông: duyệt từng đỉnh, gặp đỉnh chưa thăm thì bắt đầu một lần BFS hoặc DFS mới, tức một thành phần mới. Ở đây có ba thành phần. Ứng dụng: nhóm bạn trong mạng xã hội, tô màu vùng, kiểm tra mạng còn liên thông.'),
    (170.65, 'Tóm lại: BFS dùng hàng đợi cho đường đi ngắn nhất, DFS dùng ngăn xếp để tìm chu trình, và cả hai đều đếm được thành phần liên thông.'),
])


REELS['dijkstra'] = ('dijkstra.py', 'Dijkstra', 'dijkstra-shortest-path.mp4', [
    (0.4, 'Dijkstra: đường đi ngắn nhất từ một đỉnh.'),
    (5.0, 'Đồ thị có hướng, số trên cạnh là độ dài. Đường ít cạnh nhất có phải ngắn nhất? Chưa chắc.'),
    (17.85, 'Hai thao tác. Đê của vê là độ dài tốt nhất tìm được tới vê, ban đầu của ét bằng không, còn lại vô cực. Relax cạnh: đi qua u mà ngắn hơn thì cập nhật. Rồi chốt đỉnh có đê nhỏ nhất.'),
    (33.5, 'Chạy Dijkstra từ ét. Ban đầu chỉ có ét trong hàng đợi. Mỗi lần ta lấy ra đỉnh có đê nhỏ nhất và chốt nó, rồi relax các cạnh đi ra: lấy đê của u cộng trọng số, so với đê của vê. Nhỏ hơn thì cập nhật, không nhỏ hơn thì giữ nguyên.'),
    (75.0, 'Đỉnh nào đã chốt thì khoảng cách của nó không đổi nữa. Khi hàng đợi rỗng, mọi đỉnh đều có đường ngắn nhất.'),
    (101.65, 'Cây đường đi ngắn nhất: mỗi đỉnh nhớ cạnh cuối làm đê của nó giảm. Tới e là năm cạnh, dài tám, ngắn hơn đường ba cạnh dài mười.'),
    (113.6, 'Vì sao chốt là đúng? Khi chốt u, đê của u nhỏ nhất trong các đỉnh đang chờ. Đường khác tới u phải qua một đỉnh đang chờ, nên không thể ngắn hơn. Điểm mấu chốt là mọi trọng số không âm.'),
    (128.45, 'Khi có cạnh âm. Cạnh bê a có trọng số trừ hai. Dijkstra chốt a quá sớm, rồi cạnh âm làm một đường đi vòng về sau lại rẻ hơn, nhưng a đã chốt nên không được sửa. Dijkstra cho đê của a bằng hai, của xê bằng ba. Đúng ra đường ét, bê, a dài một, nên đê của xê là hai. Có cạnh âm thì dùng Bellman Ford, và nó phát hiện được cả chu trình âm.'),
    (165.2, 'Tóm tắt: dùng hàng đợi ưu tiên, độ phức tạp ô của vê cộng e nhân lô-ga vê. Dùng trong định tuyến mạng, bản đồ, game, nhưng chỉ khi mọi trọng số không âm.'),
])


REELS['mst'] = ('mst.py', 'Mst', 'mst-kruskal-prim.mp4', [
    (0.4, 'Cây khung nhỏ nhất: nối mọi đỉnh với chi phí thấp nhất.'),
    (5.0, 'Sáu thành phố, số trên cạnh là chi phí kéo cáp. Cần chọn các cạnh sao cho mọi đỉnh liên thông và tổng chi phí nhỏ nhất. Tập tối ưu không có chu trình, nên là cây, đúng năm cạnh.'),
    (19.77, 'Thử hết mọi cây khung? Đồ thị này có năm mươi lăm cây, nhưng mười đỉnh đã có một trăm triệu cây. Cần cách chọn tham lam, mỗi bước lấy cạnh rẻ nhất mà vẫn an toàn.'),
    (33.62, 'Kruskal: cạnh nhẹ trước. Xét các cạnh theo trọng số tăng dần, cạnh nào tạo chu trình thì bỏ. Ta dùng Union Find để biết hai đỉnh có cùng thành phần không. Hai đầu ở hai thành phần khác nhau thì lấy cạnh, cùng thành phần thì bỏ vì tạo chu trình. Đủ năm cạnh thì dừng, khỏi xét cạnh e ép chín. Kết quả: đê e, a đê, bê e, xê e, xê ép, tổng hai mươi.'),
    (84.27, 'Prim lớn dần từ một đỉnh. Bắt đầu từ a, mỗi bước lấy cạnh nhẹ nhất đi từ tập ét ra ngoài, rồi thêm đỉnh mới vào ét. Cuối cùng ta có cùng năm cạnh, cùng tổng hai mươi như Kruskal. Thứ tự chọn khác nhau: Prim lấy a đê trước đê e. Nếu trọng số khác nhau đôi một thì cây khung nhỏ nhất là duy nhất.'),
    (130.12, 'Vì sao tham lam lại đúng? Tính chất lát cắt: chia đỉnh thành ét và phần còn lại, cạnh nhẹ nhất băng qua lát cắt luôn nằm trong cây khung nhỏ nhất. Giả sử có cây không chứa đê e, tổng hai mươi ba. Thêm đê e vào thì có chu trình, bỏ cạnh a bê, giữ đê e, tổng giảm xuống hai mươi.'),
    (157.17, 'Kruskal hay Prim? Cả hai cho cùng một tổng nhỏ nhất. Đừng nhầm với đường đi ngắn nhất của Dijkstra.'),
])


REELS['tree-traversal'] = ('tree_traversal.py', 'TreeTraversal', 'tree-traversal.mp4', [
    (0.4, 'Duyệt cây nhị phân: thăm mọi nút, mỗi nút đúng một lần.'),
    (6.37, 'Ba thứ tự DFS khác nhau ở lúc thăm gốc. Preorder thăm gốc trước, inorder thăm gốc ở giữa, postorder thăm gốc sau cùng. Mẹo: đi vòng quanh cây sát mép, bắt đầu từ bên trái gốc, gặp cạnh trái của nút thì ghi preorder, gặp đáy thì ghi inorder, gặp cạnh phải thì ghi postorder. Với cây này ta được a bê đê e xê ép, đê bê e a xê ép, và đê e bê ép xê a.'),
    (42.85, 'Cây biểu thức ba cộng bốn nhân năm trừ hai. Preorder cho ra tiền tố, postorder cho ra hậu tố, inorder cần thêm ngoặc để giữ đúng cấu trúc. Tính hậu tố bằng ngăn xếp: gặp số thì đẩy vào, gặp phép toán thì lấy hai số trên cùng ra tính rồi đẩy kết quả. Ba cộng bốn được bảy, năm trừ hai được ba, bảy nhân ba bằng hai mươi mốt.'),
    (79.93, 'Inorder trên cây tìm kiếm nhị phân. Chèn lần lượt tám, ba, mười, một, sáu, mười bốn, bốn, bảy: nhỏ hơn đi trái, lớn hơn đi phải. Inorder luôn cho dãy tăng dần, vì mọi khóa bên trái nhỏ hơn gốc, và gốc nhỏ hơn mọi khóa bên phải.'),
    (107.38, 'Level order duyệt theo mức bằng hàng đợi: lấy nút đầu hàng đợi, thăm nó, đẩy các con vào cuối. Đây chính là BFS trên cây. Mọi cách duyệt đều ô của en, vì mỗi nút vào ra đúng một lần.'),
    (132.6, 'Dựng lại cây từ hai dãy duyệt. Phần tử đầu của preorder là gốc a. Trong inorder, bên trái a là cây con trái đê bê e, bên phải là xê ép. Lặp lại cho cây trái: gốc bê, đê bên trái, e bên phải. Cây phải: gốc xê, ép là con phải. Chỉ có preorder và postorder thì không đủ, vì hai cây khác nhau có thể cùng hai dãy.'),
    (165.95, 'Chọn cách duyệt nào còn tùy mục đích: preorder để sao chép, inorder cho dãy tăng, postorder để tính biểu thức, level order theo từng mức. Bài sau là cây Huffman.'),
])
