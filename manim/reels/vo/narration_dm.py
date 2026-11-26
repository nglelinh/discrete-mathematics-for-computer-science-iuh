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


REELS['huffman'] = ('huffman.py', 'Huffman', 'huffman-coding.mp4', [
    (0.4, 'Mã Huffman: ký tự hay gặp mã ngắn, ký tự hiếm mã dài.'),
    (7.25, 'Bước không: đếm tần suất. ABRACADABRA có mười một ký tự: a năm lần, bê hai, rờ hai, xê một, đê một. Mã cố định cần ba bit mỗi ký tự, tổng ba mươi ba bit. Chữ a gặp năm lần mà vẫn tốn ba bit: phí!'),
    (28.15, 'Gộp hai nút nhẹ nhất, lặp lại. Xê một cộng đê một thành hai. Bê hai cộng rờ hai thành bốn, hòa thì lấy theo thứ tự. Hai cộng bốn thành sáu. Cuối cùng a năm cộng sáu thành mười một: còn một nút, đó là gốc. Quy ước nhánh trái là không, nhánh phải là một. Tổng cộng chỉ hai mươi ba bit thay vì ba mươi ba, tiết kiệm ba mươi phần trăm, trung bình hai phẩy không chín bit mỗi ký tự.'),
    (75.27, 'Mã hóa và giải mã. Thay mỗi ký tự bằng mã của nó rồi bỏ khoảng trắng, chỉ còn chuỗi bit. Không cần dấu phân cách, vì ký tự chỉ nằm ở lá, nên không mã nào là tiền tố của mã khác. Ta gọi đó là prefix free.'),
    (103.75, 'Nếu mã không prefix free thì sao? Thử a bằng không, bê bằng không một, xê bằng một. Nhận chuỗi không một: đọc là bê, hay a rồi xê? Mã không của a là tiền tố của mã không một của bê, nên mập mờ. Cây Huffman tránh được điều này, vì đường đến một lá không đi qua lá khác.'),
    (128.27, 'Luyện tập với MISSISSIPPI. Tần suất: i bốn, ét bốn, pê hai, em một, tổng mười một ký tự. Huffman cho bốn cộng tám cộng sáu cộng ba, bằng hai mươi mốt bit. Mã cố định hai bit cho bốn ký tự thì mười một nhân hai bằng hai mươi hai bit. Chỉ lợi một bit: tần suất khá đều thì Huffman lợi ít, tần suất càng lệch như ABRACADABRA càng lợi nhiều.'),
    (160.93, 'Vì sao tham lam lại tối ưu? Số bit bằng tổng tần suất nhân độ sâu của lá. Hai ký tự hiếm nhất nên nằm sâu nhất, làm hai lá anh em, đổi chỗ không làm tổng tăng. Gộp chúng thành một ký tự mới, bài toán nhỏ đi một ký tự, rồi lặp lại bằng quy nạp. Huffman có trong ZIP, PNG, JPEG, MP3.'),
])


REELS['big-o'] = ('big_o.py', 'BigO', 'big-o-growth.mp4', [
    (0.4, 'Big O: khi n lớn dần, thuật toán nào chậm đi nhanh hơn?'),
    (7.12, 'Máy chạy một tỉ phép tính mỗi giây. Hai mũ bốn mươi phép tính mất khoảng mười tám phút, nhưng hai mũ sáu mươi phép là ba mươi sáu năm! Trong khi đó sáu mươi bình phương chỉ là ba nghìn sáu trăm phép, chưa tới một phần triệu giây.'),
    (31.87, 'Hãy nhìn các đường tăng trưởng. Hai mũ n vượt khỏi khung từ n khoảng bảy, còn n bình phương chậm hơn nhưng vẫn bỏ xa n log n. Big O chỉ quan tâm hình dạng đường cong khi n lớn, không quan tâm vài giá trị đầu.'),
    (52.27, 'Định nghĩa: f của n là O của g của n nếu có hằng số c dương và n không, để f của n nhỏ hơn hoặc bằng c nhân g của n với mọi n từ n không trở đi. Ví dụ, từ n bằng sáu trở đi f luôn nhỏ hơn bốn n bình phương, nên f là O của n bình phương. Chọn c bằng mười cũng được: c và n không không duy nhất.'),
    (75.65, 'Ô mê ga là chặn dưới, Thê ta là đúng cỡ: vừa O vừa Ô mê ga. Khi n từ sáu, f bị kẹp giữa ba n bình phương và bốn n bình phương, nên f là Thê ta của n bình phương. O chỉ nói không lớn hơn, Thê ta mới là đúng cỡ.'),
    (95.98, 'Quy tắc rút gọn: bỏ hằng số nhân, giữ số hạng lớn nhất, cơ số log không quan trọng. Vòng lặp nối tiếp thì cộng, lồng nhau thì nhân. Thứ tự tăng: một, log n, n, n log n, n bình phương, n mũ ba, hai mũ n, n giai thừa.'),
    (117.13, 'Đếm bước trong code. Vòng lồng nhau chạy n nhân n trừ một chia hai lần, là Thê ta của n bình phương. Vòng chia đôi mỗi lần, một nghìn chỉ cần chín vòng, là Thê ta của log n. Lồng vòng chia đôi trong vòng n thì được n log n.'),
    (135.77, 'Những bẫy thường gặp. O chỉ là chặn trên: n là O của n bình phương vẫn đúng, nhưng Thê ta của n mới chính xác. Hằng số vẫn quan trọng khi n nhỏ. Hai mũ n cộng một vẫn là O của hai mũ n, nhưng bốn mũ n thì không. N bình phương không là O của n. Và O của n bình phương không có nghĩa là chạy n bình phương giây.'),
    (161.42, 'Tóm tắt: O là chặn trên, Ô mê ga là chặn dưới, Thê ta là đúng cỡ. Chứng minh là tìm c và n không. Bỏ hằng số, giữ số hạng trội. Hai mũ n bùng nổ, nên tránh thuật toán mũ khi n lớn.'),
])


REELS['cantor'] = ('cantor.py', 'Cantor', 'cantor-diagonal.mp4', [
    (0.4, 'Đường chéo Cantor: có vô hạn lớn hơn vô hạn không?'),
    (6.87, 'Một tập đếm được nếu ta đánh số được các phần tử thành a một, a hai, a ba, mà không bỏ sót. Số nguyên có gấp đôi số tự nhiên không? Không: xếp không, một, trừ một, hai, trừ hai, ba, trừ ba, mỗi số nguyên có đúng một số thứ tự. Với tập vô hạn, tập con thật sự vẫn có thể cùng lực lượng.'),
    (31.28, 'Khách sạn Hilbert có vô hạn phòng và đã kín chỗ. Một khách mới đến: khách phòng n chuyển sang phòng n cộng một, phòng một trống. Vô hạn khách mới thì khách phòng n chuyển sang phòng hai n, dành hết các phòng lẻ cho khách mới.'),
    (50.2, 'Ngay cả tập số hữu tỉ cũng đếm được. Mọi phân số dương p trên q đều nằm trong một bảng vô hạn. Đi theo từng hàng thì không bao giờ xuống được hàng hai, nhưng đi theo đường chéo thì đến được mọi ô. Bỏ qua các phân số không tối giản vì đã gặp giá trị đó rồi, rồi xen kẽ thêm không và các số âm như với số nguyên. Vậy Q cũng đếm được.'),
    (79.12, 'Thử liệt kê các dãy nhị phân vô hạn. Giả sử có một danh sách s một, s hai, s ba, chứa mọi dãy không một vô hạn. Nhìn đường chéo: bit thứ k của dãy thứ k. Lật từng bit đường chéo, không thành một, một thành không, ta được dãy mới d. D khác s một ở bit thứ nhất, khác s hai ở bit thứ hai, nên d khác mọi dãy trong danh sách. Mâu thuẫn: tập các dãy không một vô hạn không đếm được.'),
    (111.25, 'Cùng ý tưởng với số thực trong khoảng không đến một. Quy tắc: chữ số đường chéo là năm thì đổi thành bốn, khác năm thì đổi thành năm, chỉ dùng bốn và năm để tránh không phẩy bốn chín chín bằng không phẩy năm. Số mới x khác mọi số trong danh sách, nên số thực không đếm được. Theo định lý Cantor, có vô số cỡ vô hạn khác nhau.'),
    (136.52, 'Đường chéo trong tin học: bài toán dừng. Các chương trình đếm được. Bảng: hàng là chương trình, cột là đầu vào, một là dừng, không là chạy mãi. Giả sử có H đoán đúng mọi ô, dựng D làm ngược với ô n n. D trùng hàng k nào đó, nhưng khác ở ô k k: mâu thuẫn! Bài toán dừng không giải được, Turing, một chín ba sáu.'),
    (162.67, 'Tóm tắt: N, Z, Q đều đếm được. Đường chéo dựng phần tử nằm ngoài danh sách, nên số thực không đếm được. Cùng kỹ thuật cho thấy bài toán dừng không giải được.'),
])


REELS['fibonacci'] = ('fibonacci.py', 'Fibonacci', 'fibonacci-binet.mp4', [
    (0.4, 'Fibonacci: từ hình xoắn ốc, tỉ lệ vàng đến công thức Binet.'),
    (6.25, 'Dãy một, một, hai, ba, năm, tám, mười ba: mỗi số bằng tổng hai số trước. Ghép hình vuông cạnh F n, mỗi hình vuông mới có cạnh bằng tổng hai cạnh trước.'),
    (20.02, 'Xét tỉ số hai số liên tiếp, F n cộng một chia F n. Nó tiến dần tới phi, bằng một cộng căn năm chia hai, khoảng một phẩy sáu một tám. Vì sao lại ra đúng số này? Câu trả lời nằm ở phương trình đặc trưng.'),
    (39.33, 'Phương trình đặc trưng: thay F n bằng r mũ n, chia hai vế cho r mũ n trừ hai, ta được r bình phương bằng r cộng một. Hai nghiệm là phi bằng một cộng căn năm chia hai, và psi bằng một trừ căn năm chia hai. Truy hồi tuyến tính nên mọi tổ hợp A phi mũ n cộng B psi mũ n đều thỏa mãn.'),
    (64.98, 'Tìm A, B từ điều kiện đầu. F không bằng không cho B bằng trừ A. F một bằng một cho A nhân phi trừ psi bằng một, mà phi trừ psi bằng căn năm, nên A bằng một chia căn năm. Đó là công thức Binet. Thử n bằng mười ra đúng năm mươi lăm.'),
    (92.33, 'Vì sao tỉ số tiến tới phi? Vì trị tuyệt đối của psi khoảng không phẩy sáu một tám, nhỏ hơn một, nên psi mũ n tiến về không. Do đó F n xấp xỉ phi mũ n chia căn năm, và tỉ số F n cộng một chia F n xấp xỉ phi.'),
    (113.73, 'Khi phương trình có nghiệm kép. Với a n bằng bốn a n trừ một trừ bốn a n trừ hai, ta có r bằng hai kép. Thử A cộng B nhân hai mũ n chỉ còn một hằng số, sai. Dạng đúng là A cộng B n, nhân hai mũ n. Từ a không bằng một và a một bằng sáu, được A bằng một, B bằng hai: a n bằng một cộng hai n, nhân hai mũ n.'),
    (144.68, 'Ba bước giải truy hồi bậc hai: viết phương trình đặc trưng; nghiệm khác nhau thì A r một mũ n cộng B r hai mũ n, nghiệm kép thì A cộng B n nhân r mũ n; rồi dùng a không, a một để tìm A, B.'),
])


REELS['divide-conquer'] = ('divide_conquer.py', 'DivideConquer', 'divide-and-conquer-master.mp4', [
    (0.4, 'Hệ thức truy hồi chia để trị: T n bằng a nhân T n chia b, cộng f n.'),
    (8.18, 'Cây đệ quy cho T n bằng hai T n chia hai cộng n, tức merge sort. Với n bằng mười sáu, mỗi tầng tốn đúng n. Có bốn tầng chia và một tầng lá. Vậy T mười sáu bằng mười sáu nhân bốn cộng mười sáu bằng tám mươi, nên T n là Thê ta của n log n.'),
    (33.15, 'Cách khác là thế ngược. Thay T n chia hai bằng hai T n chia bốn cộng n chia hai, rồi lặp lại. Dừng khi n chia hai mũ j bằng một, tức j bằng log hai của n, ta được n log n cộng n. Cùng kết quả với cây đệ quy: mười sáu nhân bốn cộng mười sáu bằng tám mươi.'),
    (59.12, 'Tìm kiếm nhị phân, T n bằng T n chia hai cộng một: mỗi bước bỏ một nửa. Mỗi tầng một nút, nên T n là Thê ta của log n. Một tỉ phần tử chỉ cần khoảng ba mươi phép so sánh.'),
    (76.38, 'Với T n bằng bốn T n chia hai cộng n, số nút tăng nhanh hơn chi phí giảm. Chi phí mỗi tầng nhân đôi, tổng bằng hai n bình phương trừ n, tầng lá chiếm phần lớn, nên T n là Thê ta của n bình phương.'),
    (93.63, 'Với T n bằng hai T n chia hai cộng n bình phương, chi phí gộp lớn nên gốc nặng nhất. Tầng i tốn n bình phương chia hai mũ i, giảm một nửa mỗi tầng, tổng nhỏ hơn hai n bình phương. Cũng là Thê ta của n bình phương, nhưng ở đây gốc thắng.'),
    (112.58, 'Định lý thợ. Đặt k bằng log a chia log b, số lá là n mũ k. Trường hợp một: f nhỏ hơn n mũ k, lá thắng, T n là Thê ta của n mũ k. Trường hợp hai: f cùng cỡ n mũ k, các tầng ngang nhau, thêm thừa số log n. Trường hợp ba: f lớn hơn, gốc thắng, T n là Thê ta của f n.'),
    (136.35, 'Áp dụng định lý thợ: merge sort và tìm kiếm nhị phân thuộc trường hợp hai. Karatsuba ra n mũ một phẩy năm tám lăm, Strassen ra n mũ hai phẩy tám một. Với n log n làm chi phí gộp thì không áp dụng được, ta vẽ cây và được n log bình phương n.'),
    (158.48, 'Tóm tắt: vẽ cây đệ quy, cộng chi phí theo từng tầng. Tầng bằng nhau thì thêm log n, tăng dần thì lá thắng, giảm dần thì gốc thắng.'),
])


REELS['dnf-cnf'] = ('dnf_cnf.py', 'DnfCnf', 'dnf-cnf-normal-forms.mp4', [
    (0.4, 'Dạng chuẩn tắc: DNF và CNF.'),
    (4.3, 'Literal là một biến, hoặc phủ định của một biến. Phủ định của cả công thức ghép thì không phải literal.'),
    (14.55, 'DNF là tuyển của các hội: các khung và nối với nhau bằng hoặc. CNF là hội của các tuyển: các clause hoặc nối với nhau bằng và. Hai dạng đổi vai và, hoặc cho nhau.'),
    (30.8, 'Từ bảng chân trị ra DNF: chỉ xét các hàng có f bằng đúng. Mỗi hàng cho một hội, biến đúng thì giữ nguyên, biến sai thì thêm phủ định. Nối bốn hội đó bằng hoặc, ta được DNF đầy đủ của f.'),
    (53.65, 'Từ bảng chân trị ra CNF thì ngược lại: chỉ xét các hàng có f bằng sai. Mỗi hàng cho một mệnh đề con, biến đúng thì thêm phủ định, biến sai thì giữ nguyên. Nối bốn mệnh đề đó bằng và, ta được CNF đầy đủ của f.'),
    (79.7, 'Đưa công thức về DNF, CNF, với g bằng p tương đương q, suy ra r. Ba việc: bỏ suy ra và tương đương, đẩy phủ định vào trong, rồi phân phối. Dùng De Morgan và phủ định kép, ta được p và không q, hoặc không p và q, hoặc r. Đã là DNF.'),
    (107.05, 'Muốn CNF thì phân phối hoặc qua và. Rút gọn p hoặc không p bằng đúng, ta được p hoặc q hoặc r, và không p hoặc không q hoặc r. Đã là CNF.'),
    (124.1, 'Kiểm tra: ba cột g, DNF và CNF giống nhau ở cả tám hàng.'),
    (137.35, 'Vì sao cần CNF? Mọi công thức đều có cả DNF lẫn CNF. SAT solver nhận đầu vào là CNF: mỗi mệnh đề con là một ràng buộc, solver tìm cách gán sao cho mọi ràng buộc cùng đúng.'),
    (153.7, 'Tóm tắt: biến đổi bằng luật, bỏ suy ra và tương đương, đẩy phủ định vào trong, rồi phân phối.'),
])


REELS['karnaugh'] = ('graycode.py', 'GrayCode', 'karnaugh-maps-gray-code.mp4', [
    (0.4, 'Bản đồ Karnaugh: khoanh nhóm các ô một trên lưới sắp theo mã Gray.'),
    (6.5, 'Mã Gray: phản chiếu dãy rồi thêm không, thêm một. Hai mã liền nhau khác đúng một bit, kể cả mã cuối với mã đầu. Thứ tự nhị phân thường thì không: không một sang một không đổi cả hai bit.'),
    (23.88, 'Mã Gray ba bit là đi dọc các cạnh của khối lập phương.'),
    (35.43, 'Vì sao cần khác đúng một biến? Biến đổi giá trị trong nhóm thì bị triệt. Gộp hai ô bỏ một biến, bốn ô bỏ hai biến, tám ô bỏ ba biến. Nhóm phải là hình chữ nhật có một, hai, bốn, tám ô.'),
    (51.68, 'K-map hai biến dùng thứ tự Gray cho trục, nên hai ô cạnh nhau chỉ khác một biến. Cột y bằng một: x đổi, còn y. Hàng x bằng một: y đổi, còn x. Ô mười một nằm trong cả hai nhóm, được phép. Vậy F bằng x cộng y.'),
    (73.13, 'K-map ba biến. Hàng xy theo thứ tự Gray: không không, không một, một một, một không. F bằng tổng các minterm không, một, hai, năm, bảy. Khoanh các nhóm lớn nhất, rồi đọc mỗi nhóm thành một hạng tử. Có cách khoanh khác cũng tối tiểu, cùng ba hạng tử, sáu literal.'),
    (102.58, 'Mép trên kề mép dưới: hàng không không và hàng một không chỉ khác bit x, như cuộn lưới thành ống. Hai minterm không và bốn cho F bằng y phủ định z phủ định.'),
    (115.33, 'K-map bốn biến: hàng xy và cột zw đều theo Gray, cột trái kề cột phải, hàng trên kề hàng dưới. Với mười hai minterm, tám ô ở hai cột giữa cho w, các ô còn lại gom thành y phủ định. Vậy F bằng y phủ định cộng w: mỗi minterm bốn literal, rút còn hai.'),
    (140.88, 'Bốn góc cũng là một nhóm. Với F bằng tổng các minterm không, hai, năm, bảy, tám, mười, mười ba, mười lăm: bốn góc cho y phủ định w phủ định, khối hai nhân hai ở giữa cho y w. Vậy F bằng y phủ định w phủ định cộng y w.'),
    (160.63, 'Ô don\'t care, ký hiệu X. F bằng một tại m không, một, ba; không quan tâm tại m năm, bảy. Coi X là một thì được x phủ định y phủ định cộng z, nhóm to hơn. X chỉ dùng khi làm nhóm to hơn, không bắt buộc phải phủ.'),
    (180.78, 'Quy tắc khoanh nhóm: nhóm to nhất có thể, kích thước lũy thừa của hai. Đọc nhóm: biến đổi giá trị thì bỏ, biến luôn một giữ nguyên, biến luôn không lấy phủ định.'),
])


REELS['incl-excl'] = ('incl_excl.py', 'InclExcl', 'inclusion-exclusion.mp4', [
    (0.4, 'Nguyên lý bù trừ: cộng các tập, trừ phần đếm trùng, rồi cộng lại phần trừ quá tay.'),
    (6.75, 'Lớp năm mươi sinh viên: ba mươi học Anh, hai mươi học Pháp, mười học cả hai. Cộng ba mươi với hai mươi là sai, vì mười bạn ở phần giao bị đếm hai lần. Đúng là ba mươi cộng hai mươi trừ mười bằng bốn mươi, còn mười bạn không học môn nào.'),
    (28.03, 'Ba tập thì mỗi vùng bị đếm mấy lần? Bước một: cộng A, B, C. Phần giao đôi bị đếm hai lần, phần giữa ba lần. Bước hai: trừ các giao đôi A B, A C, B C. Phần giữa bị trừ ba lần, giờ thành không. Bước ba: cộng giao ba tập. Mọi vùng đều được đếm đúng một lần.'),
    (58.33, 'Từ một đến một trăm, bao nhiêu số chia hết cho hai, ba hoặc năm? Chia hết cho cả hai và ba nghĩa là chia hết cho sáu, vì hai và ba nguyên tố cùng nhau. Giao ba tập là phần nguyên của một trăm chia ba mươi, bằng ba. Tổng: năm mươi cộng ba mươi ba cộng hai mươi trừ mười sáu, trừ mười, trừ sáu, cộng ba, bằng bảy mươi bốn.'),
    (84.63, 'Kiểm tra trên lưới từ một đến một trăm: bảy mươi bốn ô được tô, hai mươi sáu ô còn trống. Dạng bù: một trăm trừ bảy mươi bốn bằng hai mươi sáu số không chia hết cho số nào. Mỗi ba mươi số liên tiếp có đúng tám số như vậy.'),
    (104.68, 'Bài tập: từ một đến một nghìn, bao nhiêu số không chia hết cho ba, năm và bảy? Đếm phần bù: số chia hết cho ít nhất một trong ba số, là sáu trăm bảy mươi lăm trừ một trăm bốn mươi mốt cộng chín, bằng năm trăm bốn mươi ba. Vậy không chia hết: một nghìn trừ năm trăm bốn mươi ba bằng bốn trăm năm mươi bảy.'),
    (134.98, 'Với n tập hợp, phần tử thuộc đúng m tập được đếm C m một trừ C m hai cộng C m ba và cứ thế, đúng một lần. N tập cho hai mũ n trừ một số hạng, bốn tập đã là mười lăm số hạng.'),
    (153.88, 'Ứng dụng: không lá thư nào đúng chỗ. Ba lá thư bỏ ngẫu nhiên vào ba phong bì, có bao nhiêu cách để không lá nào đúng? Bù trừ cho sáu trừ sáu cộng ba trừ một bằng hai. Đó là hai cách, B C A và C A B. Với bốn lá thư thì có chín cách. Bù trừ còn dùng để đếm số không chia hết, mật khẩu thiếu loại ký tự, số toàn ánh giữa hai tập.'),
])


REELS['nfa-dfa'] = ('nfa_dfa.py', 'NfaDfa', 'nfa-to-dfa-subset-construction.mp4', [
    (0.4, 'Otomat hữu hạn: từ NFA sang DFA.'),
    (5.0, 'Đây là một NFA bốn trạng thái, nhận các chuỗi bắt đầu bằng một và kết thúc bằng không một. Không tất định: ở q một đọc không thì có hai lựa chọn. Còn q ba đọc gì cũng không có cạnh, nhánh đó chết.'),
    (22.45, 'NFA chấp nhận nếu có ít nhất một cách đi kết thúc ở trạng thái chấp nhận. Ta theo dõi mọi nhánh cùng lúc bằng một tập trạng thái. Đọc một, một, không, một: tập cuối chứa q ba, nên chấp nhận. Còn chuỗi không một không một thì mọi nhánh chết ngay, tập rỗng, bị loại.'),
    (56.3, 'Ý tưởng: mỗi tập trạng thái của NFA là một trạng thái của DFA. Bắt đầu từ tập q không, gọi là A. Với mỗi tập và mỗi ký tự, lấy hợp các bước đi của từng phần tử. A đọc không ra tập rỗng, A đọc một ra B. B đọc không ra C, gồm q một và q hai. B đọc một vẫn ở B. C đọc không vẫn là C, C đọc một ra D, gồm q một và q ba. D đọc không về C, đọc một về B. Tập rỗng là trạng thái chết, đọc gì cũng quay lại chính nó. Hết tập mới, bảng xong, năm trạng thái.'),
    (107.95, 'Đây là DFA thu được: mỗi trạng thái, mỗi ký tự, đúng một cạnh. Trạng thái chấp nhận là D, vì chứa q ba. Thử một không không một: dừng ở D, chấp nhận, giống NFA. Thử một không một một không: kết thúc ở C, không phải trạng thái chấp nhận, nên loại. Chuỗi bắt đầu bằng không rơi ngay vào tập rỗng.'),
    (148.25, 'Vì sao đúng? Sau khi đọc w, DFA ở đúng tập các trạng thái NFA có thể tới bằng w. Chứng minh bằng quy nạp theo độ dài w. Cái giá là có thể tới hai mũ n trạng thái. Ký tự thứ n từ cuối là một: NFA cần n cộng một trạng thái, DFA nhỏ nhất cần hai mũ n.'),
    (166.7, 'Nên chỉ dựng các tập tới được từ trạng thái đầu.'),
])


REELS['stars-bars'] = ('stars_bars.py', 'StarsBars', 'stars-and-bars.mp4', [
    (0.4, 'Tổ hợp có lặp, hay sao và vạch: đếm cách chọn khi được lấy trùng và không xét thứ tự.'),
    (7.52, 'Chọn năm chiếc bánh từ ba loại: sô-cô-la, dâu, việt quất, mỗi loại còn rất nhiều. Chỉ quan tâm số lượng mỗi loại. Mỗi cách chọn là một dãy năm sao và hai vạch, vạch là vách ngăn giữa các loại.'),
    (32.08, 'Bảy ô, chọn hai ô làm vạch, năm ô còn lại là sao. Số cách là C bảy chọn hai, bằng hai mươi mốt. Đủ cả hai mươi mốt dãy, không thiếu, không trùng, đó là một song ánh.'),
    (59.77, 'Công thức tổng quát: C r cộng n trừ một chọn n trừ một, bằng C r cộng n trừ một chọn r. Ví dụ, x một cộng x hai cộng x ba cộng x bốn bằng mười có C mười ba chọn ba, hai trăm tám mươi sáu nghiệm. Chọn sáu viên kẹo từ bốn loại: C chín chọn sáu, tám mươi bốn. Đừng nhầm với C n chọn r thường.'),
    (89.53, 'Ràng buộc dưới thì phát trước. Với x một lớn hơn hoặc bằng hai, x hai lớn hơn hoặc bằng một, x ba lớn hơn hoặc bằng bốn, tổng bằng mười hai: đặt sẵn bảy sao, còn năm sao chia tự do, C bảy chọn hai, hai mươi mốt nghiệm.'),
    (111.7, 'Ràng buộc trên thì cần bù trừ. Ba biến tổng bằng mười, mỗi biến không quá bốn. Lấy sáu mươi sáu nghiệm tổng cộng, trừ sáu mươi ba nghiệm có biến vượt quá, cộng lại ba nghiệm trùng, ra sáu. Đúng sáu nghiệm, là các hoán vị của bốn bốn hai và bốn ba ba.'),
    (137.07, 'Luyện tập. Một: mua sáu viên kẹo từ bốn loại, có trùng loại, C chín chọn ba, tám mươi bốn cách. Hai: chia mười viên bi giống nhau cho bốn em, mỗi em ít nhất hai viên. Phát trước tám viên, còn hai viên, C năm chọn ba, mười cách.'),
    (168.47, 'Tóm lại: đổi bài toán chia thành sắp sao và vạch.'),
])


REELS['pigeon-adv'] = ('pigeon_adv.py', 'PigeonAdv', 'pigeonhole-advanced.mp4', [
    (0.4, 'Nguyên lý chuồng bồ câu nâng cao: khó nhất là chọn chuồng.'),
    (7.0, 'Dạng tổng quát: N con bồ câu vào n chuồng thì có chuồng chứa ít nhất trần của N chia n con. Chín con, bốn chuồng: có chuồng ba con. Bốn nghìn lẻ một khóa thì chắc chắn có bucket năm khóa.'),
    (26.15, 'Năm điểm trong hình vuông cạnh một. Chia thành bốn ô vuông cạnh một phần hai, thì có ô chứa hai điểm. Hai điểm đó cách nhau không quá căn hai trên hai, tức khoảng bảy phần mười. Không thể tốt hơn.'),
    (53.1, 'Chín điểm trong hình vuông, không ba điểm thẳng hàng. Có ô chứa ba điểm, tam giác có diện tích không quá một phần tám.'),
    (65.95, 'Chọn sáu số từ một đến mười. Lập năm chuồng là các cặp có tổng mười một. Sáu số, năm chuồng, nên có hai số cùng chuồng, tổng mười một. Với năm số thì chưa chắc.'),
    (85.8, 'Bảy số nguyên bất kỳ luôn có đoạn liên tiếp có tổng chia hết cho bảy. Xét bảy tổng riêng đầu tiên. Nếu có tổng dư không thì xong. Nếu không, chỉ có sáu số dư khác không, nên hai tổng cùng số dư. Hiệu của chúng là đoạn cần tìm.'),
    (118.35, 'Erdős Szekeres: dãy mười số khác nhau luôn có dãy con tăng hoặc giảm dài bốn. Gán mỗi số một nhãn: độ dài dãy tăng và giảm dài nhất kết thúc tại đó. Mười nhãn đôi một khác nhau. Nếu mọi độ dài không quá ba thì chỉ có chín nhãn, vô lý.'),
    (156.7, 'Mẹo: bồ câu nhiều hơn chuồng thì va chạm chắc chắn xảy ra.'),
])
