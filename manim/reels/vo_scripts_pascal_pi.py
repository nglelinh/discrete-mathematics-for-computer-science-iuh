"""Lời dẫn tiếng Việt cho reel pascal-to-pi (bài 07-04).

Định dạng giống vo_scripts_batch2/3 của repo Optimization: REELS[tên] = (file, Scene, [(giai đoạn, offset, lời dẫn)]).
Mỗi giai đoạn (mục) có một đoạn lời dẫn, bắt đầu sau mốc đầu giai đoạn một khoảng offset (giây).
TIMING đo từ bản render -qh tiếng Việt (VO_LOG của pascal_pi.py, 30 fps) đã có pads: vo/pascal_pi_pads.json
= {mục: giây} thêm khoảng dừng cuối mục (mục 3: 0,5 s; mục 5: 3,2 s) để đoạn thu không tràn sang mục sau.
Lời dẫn viết theo cách đọc (số, chữ Hy Lạp, k/n/m đánh vần: ca, en, em; Leibniz đọc là Lai-bờ-nít).

Đã thu bằng ElevenLabs (giọng "Trường - Calm and Clear Educator", voice_id U0vnF55XGy05G83azOfJ, model eleven_v3),
mỗi giai đoạn một đoạn, ghép bằng build_vo_track + mux của skills/course-manim-voice (loudnorm từng đoạn, không cắt khoảng lặng).
Độ dài đoạn thu (giây): 32,24; 35,04; 31,20; 39,36; 46,24; 38,64; 9,68. File mp3 để trong manim/reels/media/vo_pascal_pi/ (gitignore).
"""

REELS = {
    'pascal-to-pi': ('pascal_pi.py', 'PascalPi', [
        (1, 0.4, 'Đây là tam giác Pascal. Hàng trên cùng chỉ có số một, và mỗi hàng bên dưới đều bắt đầu, kết thúc bằng một. Số ở giữa bằng tổng hai số đứng ngay phía trên nó. Hàng ba có hai số ba, nên hàng bốn có số ba cộng ba bằng sáu. Viết gọn: tổ hợp chập ca của en bằng tổ hợp chập ca trừ một của en trừ một, cộng tổ hợp chập ca của en trừ một. Số này nằm ở hàng en, vị trí ca, đếm từ không. Cứ thế dựng tiếp đến hàng mười hai, mà chỉ cần phép cộng.'),
        (2, 0.5, 'Mỗi đường chéo chạy xuống, song song với cạnh trái. Đường chéo đầu tiên toàn số một. Đường chéo thứ hai là các số tự nhiên. Đường chéo thứ ba là số tam giác một, ba, sáu, mười, bằng số cặp chọn từ en phần tử. Đường chéo tiếp theo là số bộ ba chọn từ en phần tử: một, bốn, mười, hai mươi, ba mươi lăm. Đây là dãy ta cần. Vì sao? Lấy số hai mươi ở hàng sáu: nó bằng một cộng ba cộng sáu cộng mười. Đó là đồng nhất thức cây gậy khúc côn cầu.'),
        (3, 0.5, 'Giờ lấy dãy này cách một hàng: hàng bốn, sáu, tám, mười, mười hai, được bốn, hai mươi, năm mươi sáu, một trăm hai mươi, hai trăm hai mươi. Cách một hàng nghĩa là en bằng hai ca cộng hai, và số này bằng hai ca cộng hai, nhân hai ca cộng một, nhân hai ca, chia sáu. Đảo lại, bốn chia ba số liên tiếp bằng hai phần ba chia số trên tam giác Pascal. Thử ca bằng một: cả hai vế đều là một phần sáu.'),
        (4, 1.0, 'Thêm dấu cộng trừ xen kẽ, ta có chuỗi của Nilakantha, nhà toán học Ấn Độ thế kỷ mười lăm: pi bằng ba cộng hai phần ba nhân một phần bốn trừ một phần hai mươi, và cứ thế. Mình tính tay vài số hạng: ca, số trên tam giác Pascal, số hạng hai phần ba chia số đó, và tổng riêng. Với ca bằng một được ba phẩy một sáu sáu bảy. Với ca bằng hai còn ba phẩy một ba ba ba. Giá trị nhảy lên xuống quanh pi. Vẽ ra, các điểm rơi lần lượt trên và dưới pi. Dấu đan xen, số hạng giảm dần, nên pi luôn nằm giữa hai tổng riêng liên tiếp.'),
        (5, 1.0, 'Vì sao đúng bằng pi? Bước một: đặt em bằng hai ca, tách số hạng thành phân thức đơn giản, hai trên em, trừ bốn trên em cộng một, cộng hai trên em cộng hai. Thử em bằng hai: cả hai vế là một phần sáu. Bước hai: gom hai phần mẫu chẵn thành một trên ca cộng một trên ca cộng một. Cộng đan dấu thì triệt tiêu từng cặp, chỉ còn số một. Bước ba: phần còn lại là trừ bốn trên hai ca cộng một. Theo chuỗi Lai-bờ-nít, nó bằng trừ bốn nhân một trừ pi chia bốn, tức pi trừ bốn. Cộng lại: một cộng pi trừ bốn bằng pi trừ ba, nên ba cộng pi trừ ba đúng bằng pi.'),
        (6, 1.0, 'Hội tụ nhanh đến đâu? So với chuỗi Lai-bờ-nít: đường xanh hạ rất chậm, đường vàng của Nilakantha dốc hơn nhiều. Sai số Lai-bờ-nít cỡ một trên ca. Nilakantha có ba thừa số dưới mẫu, và nhờ đan dấu sai số chỉ cỡ một trên bốn ca mũ ba. Tăng ca gấp mười, Nilakantha thêm ba chữ số, Lai-bờ-nít thêm một. Chữ số vàng là chữ số đúng. Sau một nghìn số hạng, Nilakantha đúng chín chữ số thập phân, Lai-bờ-nít mới đúng hai. Công bằng mà nói, cần một nghìn bảy trăm lẻ chín số hạng mới đúng mười chữ số: nhanh hơn Lai-bờ-nít nhiều, nhưng chưa phải nhanh nhất.'),
        (7, 1.0, 'Tóm lại: tam giác Pascal chứa sẵn các mẫu số của chuỗi Nilakantha. Tách phân thức và chuỗi Lai-bờ-nít cho đúng pi, sai số giảm như một chia ca mũ ba.'),
    ]),
}

TIMING = {
    'pascal-to-pi': {
        'duration': 257.73,
        'stages': [0.0, 35.77, 73.33, 106.17, 150.3, 198.5, 243.47],
        'stage_len': [35.77, 37.57, 32.83, 44.13, 48.2, 44.97, 14.27],
        'captions': [
            (0.4, 1, 'Tam giác Pascal: hàng trên cùng là 1, mỗi hàng bắt đầu và kết thúc bằng 1.'),
            (8.93, 1, 'Số ở giữa bằng tổng hai số ngay phía trên. Ví dụ hàng 4: 3 + 3 = 6.'),
            (18.23, 1, 'C(n, k) = C(n−1, k−1) + C(n−1, k), với C(n, k) là số cách chọn k phần tử trong n phần tử.'),
            (30.43, 1, 'Dựng tiếp đến hàng 12. Chỉ cần phép cộng.'),
            (36.23, 2, 'Mỗi đường chéo chạy xuống, song song với cạnh trái. Đường chéo 0 toàn số 1.'),
            (43.37, 2, 'Đường chéo 1 là các số tự nhiên: C(n, 1) = n.'),
            (47.07, 2, 'Đường chéo 2 là số tam giác 1, 3, 6, 10, … bằng C(n, 2): số cặp trong n phần tử.'),
            (54.13, 2, 'Đường chéo 3 là C(n, 3): 1, 4, 10, 20, 35, … số bộ ba trong n phần tử. Đây là dãy ta cần.'),
            (63.2, 2, 'Gậy khúc côn cầu: mỗi số bằng tổng các số trên đường chéo bên cạnh, ví dụ 20 = 1 + 3 + 6 + 10.'),
            (73.8, 3, 'Lấy cách một hàng: n = 4, 6, 8, 10, 12 cho 4, 20, 56, 120, 220.'),
            (85.1, 3, 'Cách một hàng nghĩa là n = 2k + 2, và C(2k+2, 3) = (2k+2)(2k+1)(2k) / 6.'),
            (94.93, 3, 'Đảo lại: 4 chia ba số liên tiếp bằng hai phần ba chia C(2k+2, 3). Thử k = 1: cả hai vế là 1/6.'),
            (107.13, 4, 'Thêm dấu cộng trừ xen kẽ ta được chuỗi Nilakantha, nhà toán học Ấn Độ, thế kỷ 15.'),
            (121.2, 4, 'Tính tay: k, số trên tam giác Pascal, số hạng, rồi tổng riêng S(k).'),
            (129.63, 4, 'k = 1: 3,1667. k = 2: 3,1333. Giá trị nhảy lên xuống quanh π.'),
            (139.87, 4, 'Các điểm rơi lần lượt trên và dưới π, dao động thu hẹp dần. π luôn nằm giữa hai tổng riêng liên tiếp.'),
            (151.27, 5, 'Bước 1: đặt m = 2k và tách số hạng thành phân thức đơn giản. Thử m = 2: cả hai vế là 1/6.'),
            (166.8, 5, 'Bước 2: hai phần chẵn gom lại, cộng đan dấu thì triệt tiêu từng cặp, chỉ còn 1.'),
            (177.33, 5, 'Bước 3: phần −4/(2k+1) bằng π − 4, nhờ chuỗi Leibniz π/4 = 1 − 1/3 + 1/5 − …'),
            (188.1, 5, '1 + (π − 4) = π − 3, nên 3 + (π − 3) = π.'),
            (199.47, 6, 'So với chuỗi Leibniz: sai số theo số số hạng k, trên thang log.'),
            (208.43, 6, 'Sai số Leibniz ≈ 1/k, sai số Nilakantha ≈ 1/(4k³). Tăng k gấp 10: thêm 3 chữ số so với 1.'),
            (223.2, 6, 'Chữ số vàng là chữ số đã đúng. Sau 1000 số hạng: 9 chữ số thập phân so với 2.'),
            (232.4, 6, 'Cần k = 1709 để đúng 10 chữ số: nhanh hơn Leibniz nhiều, nhưng chưa phải cách nhanh nhất.'),
            (244.43, 7, 'Pascal chứa sẵn các mẫu số của chuỗi Nilakantha. Sai số giảm như 1/k³.'),
        ],
    },
}
