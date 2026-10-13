"""Hashes of shipped prompt seeds; preserve history when refreshing defaults."""

_CURRENT_SEED_HASHES: dict[str, str] = {
    "asr_transcription": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "chunk_contextualizer": "35cc087891c587627f572d4876890c3a78a59e3141b217d05ffd77750ffd1af6",
    "hyde": "4c160d238359b43095b7ab223d217aa2e5f4348de6147ba33675da5f8f2aaf9d",
    "image_captioning": "0f6ea8060787d5d1c9d75243d9d2f1055b7852a2720fe226f6f0008ba2604056",
    "multi_query": "24724f4229137d869e91cf6608db656cefc400d8bd470080ed546449d5aad0dd",
    "query_contextualizer": "913562a00309bf3d2c7327e046702b9895982ac726cf17d223eaaf3b9ac67032",
    "spoken_style_answer": "1d99bca86e8dce884ac1a50d0071577eafe26b383d568225aa7f9b7ee4a02c67",
    "sys_prompt": "3f0e6c8d2e385eda15715c83f54d701cfe83fe4ffddc2cbfd6ba398ac1c599dd",
    "topic_tagger": "5d9965a1b3f84ab3000e2a68b9cbc78f579dfd49d2119ebf1547810f3b33bd0e",
}

_SUPERSEDED_SEED_HASHES: dict[str, frozenset[str]] = {
    "asr_transcription": frozenset(
        [
            "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
            "1833e2ea175d5bc9619c749be28db98b96a5ab5a1ab4c70fba9150257fda3012",
            "7b57bb71dbd53d90f35da925af5c61402e01157dac8a79066eaaffc6448c52be",
            "abc3b905e25a61bf7af684a979e6f78d68de61690f15bb087de2e0167e8b74fd",
            "cb46f504719a0400695a3ff903c3b021bcae949659a14235aafe1ed74567f271",
        ]
    ),
    "query_contextualizer": frozenset(
        [
            "0867f3358bd431ff625d65eafbd273d65928c84b49f915af6b4dc8a2c3c1f068",
            "0f9b16fb4bde42ba863708c4956647b17735a2c4fe245b0ba0c6a106a56bf4dd",
            "252bc17d09818212282eea72e38e7927dadee85ff50718d490087605c7b34872",
            "2a950346e27dd815fd42af0849caf0065f615c3bef4bff6d61d1621b39fcd066",
            "4377989d16e8e40b8849b723ab9e181293360928569ef7bbd3b66ce964c0fe9b",
            "555e02415f6163dc40a0e23878314aeb410ea0a70dd1d9a805e08ff211dc7806",
            "87f5084a4cc922681730969ed98e769550a973bc4464f45e65b5342a7cfbf91e",
            "8a3b0fc89b47a189b8e696f9383ad1f1f5023759b1ab3e01636c9455694c0b4e",
            "931a2e095ccc6443ecba0d2684d8dd32c9ffac6f484d659953f78bc96e229a0a",
            "a9ab41975b720c6b7718d88d35df69ebddf81f4a298e32c4c474a2b88f6ad463",
            "bfaaf14620d277726db22903206c85c097de1a3263d7951678ae451c279e3977",
            "c1ff41d1a86909ea608e59cc4c50e8cbf831d5368c70b0018c256816f024be0f",
            "d7b5f06862e57587c6bc2965af4a70dcc5327dfccae8172c32ab02623878f6f6",
            "db4fbb3ff1d1b91df19a31a872ae83b73a9b63b993f2f20a473d4c87725d19aa",
            "e508d9b8a1c6f46f6e4b8a461c4f064d84b0242fc6e6dbb1136a94a27de79a61",
        ]
    ),
    "spoken_style_answer": frozenset(
        [
            "03531afe7c9fa1bbf817077045183b4ca956450bc758b6a416a560b269c36cc1",
            "36d3df218283f91de2ca62693afcdd9b844ba5645fba929a98c7b7ddd0d320b1",
            "65bd5236e2d3ebab5523f4940dae60aada9a1eb9364d5fc5ff71099f6eddfd58",
            "a8677ce53e04876e189cf12d3b7886217b77e85b7643e2687a94279adb9799ae",
            "b97c409c1a06016b72ee8ef699a6c13db462461625e29c2e1e0d9c5c429fcaa0",
            "c8f0b7f5746daf42fc096d7bd7bdeec2d499edefff8c0a9ad3d2031f158f820c",
        ]
    ),
    "sys_prompt": frozenset(
        [
            "171a3ba9d9a733308fe9cbdd287c845cd73da6734af6e013174348a1b8e9aabd",
            "49110bb27e7ba96e335e3cd8293d825d9c8f4d1e2dc724f7bf2c12c016aca89c",
            "5e84b76dcf10b777167cd367b7698cd9e7bf1a1bbb9387d7b0a7b993b6cd878e",
            "8a41a40210728c184f8d5dc4bb97b76968179144b5aa7f632d0ed1ce62a0b0a8",
            "b5faacb19c176961965882bdf2f30c6dec7973de26c26c7bf18dd8f9088c07a7",
            "ce4059320f686b5ee0c5567f08f5f1ecaa2313b2d6b4aeaca77fc763cb21e989",
            "f800abc8050d94c4fc2124012840c9362d269422fea784a814e4f97f4b24bf09",
        ]
    ),
}
