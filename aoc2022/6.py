def find_start(n, data):
    for i in range(n, len(data)):
        if len(set(data[i-n:i])) == n:
            break
    return i

data = "zdrrgvvntvtzzssgcgqqbvqqzmqmrrprjjpmpwpvpqpwppfqqnvvjbjcbbrnnvwnvnqnncvvqnvqvmmdzdrzzjmmfzmztzczzjpjllgzgnzgznzpzhhvppmjjtbjbjgbjjpfphfhthpprbbzzhbzzvjjsttjwtjwjllzplzlhlqlfqfvflfvlvqvqsshccgffvzzqllpjllcqcpqcpqccbgcccvwvlldclcppcggjhhtbhbrbwbllldndhnnmnmcccvfvtftrfttlhttgltlflgflfrrftrtrgrmggbccnvccvssbmsmnsmszmmsbshbhpbhhtccnmngmnnntznttwnnmffdccrhrshhzhszslzlqqqsqhhrrvmrrhrmhrrdppshpssjhhhtzhzpzzzbrrqqhhtltgltgghlhpphmmbllczcgcrgcrcmmdjdvdssdbsshqqrprhrfrqrlldggpglplqlgqqvfqqwhqqclcwwbrbwbzzmcczqqpzpzhpzprrsbsfsgscsvsdsnntssgzsgzzdpdmmvnnnnfgngnqntnqnhqnhnrrdvrdvvhcvhcvvmffmccdndhhpghgwwdpwwsbwwwcpchcmmznnvtvfffzgffmfdmdsdrrsjjblbglgrrnllzrlrnnrzztnnnqlnlhnllnflllvjjdpdnngfnnlzlrzllrnlnznszzhhvggbqqcmqqvhqhhzfznnhthlhfllqwwghwgwnnnrcchffqnqjjmhjmjsjrjjrwjrrhbhfbhffprprhrddscddbbrzrvrcclttppvrvrlrplpffdwffwrwvvmssgjjbttpgpfplffgfwfnnmhhwghhpfptprtrzzwlwnwmwzzbmbrrdjrjzjpzpggftffglgzzdgzgbbzwzrrdzdhdbhhfppvrvrrrshrrzwwhjwwtjjhbhgbbhjhmmcvvchcfczfcffgttzbzssdqqjwjbbhthgthghthghmhlmmjwmwccfftnnddlffntnhtnhhnnldlhlthhqvhqvhhcgclcmmcnnwnqqzgzczccftfzfrrnhnjhhnlljdjhjghhchvchvchcphpnnnznhnjjlmjlmlbmmsbmbnnmqmvmhhcrcvvqffjpjzpjzjnnhsnhsslqlqvqzzmffdtfdffjrfjrjcjzjnjfjdfjfvjvddtntcttcwcqwqlqjqlqrrzccsgsgffwddrldrrhlllgppghphddqttdwtwnwlnlccmwwfnngvnvddwvwttjjsgghcchjjnvnccjljcljcljjjrttdstsmsggdbdbnddqpddbqqpbpdpgdpdnpnbnffcfrfrfhfcfgcfgcffvjvccgscshhvthvthtbhtbbmppjjrjqrjqjmjzjjjvffmbbfppndngnrnsnnmbbcmcddfzdfzdffqssfwsfwwpzpfpmpqpjqjwqqzwqwvvsddvrrdsrszrrrjqrjjqtqftthhmpmhpmhphggjsggjpppmhmzzdllcscpsswsqqjsqsvvlffmwgtmbthswfqqppsdflzhmdbcnzgdrlzccsdtptgmhfhwtbwqdhptvsvgdfdsmvsrtjjthchmbrjpmrwhgrdllphnfhrfdlgqmbrtdwcmcbphrzthflcswnhqmfhwprbgczbmsmjvbwjftgfqhbhqgzsvcpplzgctzggfljbmhsmwcwltllqgqtvhlbnpzpccbsbhpvhttdjvcnbqhlccdcclwfvcqnttlzzhqpltnnzzlnwtgppwfvmjhtmlzbzdrgbpbbmwlczdwmfhsvpnhpcqwzlnzslncdcqblvlpqfzhhszzrssvhglsllbbmjngfjlpjjvjbzbrlrmwfvzbgtzvcrshtsswhjrjvtwwbrqvtqnndndthfgfcnprpwwtffcvmllngsftrnwnjmwfljjtwnqqmphdlctvdpnsmbrhmljzmfvhcpblmwjjgqvslgslpbjzqzgzpwgssljztmztbwbqlfwrwgvwrjzvpvncqpdspgpzsjnvcrtzpnspvmnvssbgmsbpdsmcvjmtczczzsjcqcfhvcmsbsjfsssvzpvrtmmgptpcsrjslgvclflhjdpwtsmrgjjcftjmjrzrpwqlqvrqjpflbgrfhswbpcnvrrwpzqtzmqjspqqpwlcwgwgclpnwhhrrmzvvnjrjgjfqftlwjrggjgsdfvqhghmshczbbcvrmsgfdqhhmpfzqtbqwsmwfnwfwndjtlntzbbhlzlhrlzgljlmlbcwcdzbctlbqjmfpdwfcfnrbztvlwjhgmfvjcclcrwwwwvqshnfthtcccnswnfzlznlfcmcfrrsjqfvrwjvtbrwggzmdglcbzfdflrdqsjhzcjpghdmwhzrshnqqtsrccbhnlqcsclwmnvjpfqjszwrqnvbgmcdsvhntqmmnrdpbtpqwvhztmtjfvdplgzhhgsrnbwggnwzbtzwcsbrftzhvwtrwvcqrbcnqnrcmbmsvlcfbmzfcvqpwsmmfdgssnhghwjlsslmgnrqgpmbhpqzfnvztsjzjqgrzbbdpvtprwdzdszlhpcgwvdfvhtbtpfjnqnpzwplrwnfdpdclwgnrjlzzshhcchswtzrcmrfpgwjvttqfbbsdnctrtnmwqsmnfsgfgplphcrhglcrnrbzvcfrdfhdtsjmnvfwslcntttqzvhhbljzmpmlsrsblhvmvphppdmjfzwfmflcfwwtdfcndqzgsbrcppsngqfnnjtccnmfjqzhdpnnrqvhrmnrwntqrvmlzfrdszhctzjjdwqrrldtqgrztrvdfrpgprqhqrbnmpfzzlprrpqgtqmzshpcdbwgmrqhrvvgwvspqzmsrvprvsclffwhzlvgfgcsjtmnmthwfmdnfccvlbwbcrlsghhpzcvcnffvccsqjtnhhnbwgfjmqczbrfmjtmmbznspmvtcvdllbgrcvtdzpgzcjzqdjpglhbbnbvwztrdhcrcvrpbshwlmdbmpdgzzflglwgfhvngcgpwshfhzsbrmnhrftmcfqdhnmfmdzbzfgggrzchtzrhgtjpqhdglgdhdqzqpmqmtsbbjjgvtrngdvghwdmgnmdlwsvpmldlsjrtwhltfpbmqlngncwspcptphdppdmjfvtnmdrpbwzrdzcqjdnprpcddjqjhpllsrqzdpcpnplmnmwfqjtnfmnwljbsfgwlgjpwdbbqblvsqcvvgmbrhsqjcscsflcfdzbnrflmrpzhzdhzqhgvmtfjpwtfqnclplgwrjtfvrncjlqtqlrrnjsrvpwbrdcppvnjfzdrzhcltpdfgfndvqtqzvvztgzssdsvvvjwrtjmqcchbjmppqzmgwqdvmmdqbcpbmcnjsvjlwmmnvmnlzdsnsjpldgpjgsbqmpcdsvhdfhgpbggqmrdhbhvvpnzdpqtmldmfqdfchzdfgddzgvcdzgcwjlhnzjwhpwlfwhgjthjshqtzbblhflmsfvtwplfpmpndgjmhndqlhcvfhmjmmqgnjstrzqvshzbbsfqwszwccmrcjnmlsplqzwrgrcwqbmrfwljmlqtqztscrhgjdqzhvmhncvssfznpgrbrjvchsgnjjnnqqrqwsqsrgmltvgtjvpztwmsspjtqdwrbftzrbcmdthmztmnqtmmnffqjjzbvwghrsdmbbjsnnhbdcbqsbcdmwqqppcvsndzbfnsgtpptdftrfthdclqrqvmhnddmjzlnfgscfdwjljjgjnddcrzvclfqbdhprttwpmsnzvdgzwmnzznpqhlhhslwgzlczlgvbjbgqdczztzjnswphllncbsqdmbsbqqsltzmmhmhfnngbttvdsmfrpgthwpfdhsstrjssghlrrlhbmgdsvhzvlhhfvtcrrhlndgrjjcgmjwgnjtlmpmzgqgpnpsvlnthgrvsdfcnmzmthqzfpjdqjbhgmjqsqvvdldrgqwlghdlwqdbfmffgvzmptqhnvbrdbqtcjmsdnjljpbrtcvvnffvztbwfnmtvdbnshlbgvbnljntlrldbwqvqmblnvhwtw"
find_start(4, data)
find_start(14, data)