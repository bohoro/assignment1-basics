# delete me

# pretokenization

text = """
Once upon a time, there was a magical elf. She wanted to get the truth, so she searched all over. But it was not easy; the truth was hidden deep in a dark forest.
The elf was brave, so she went into the forest. She looked for the truth under trees, behind rocks, and inside caves. But it was nowhere to be found. 
Just then, the elf saw something disgusting. It was smelly and slimy and made her nose wrinkle. But the elf bravely picked it up, and guess what? There in her hands she had found the truth! 
She was so happy and quickly brought the truth back outside of the dark forest. The elf could now share the truth with all the other elves.
<|endoftext|>
"""


from collections import Counter
from collections import defaultdict

train_text = """
low low low low low
lower lower widest widest widest
newest newest newest newest newest newest
"""


def bpe_example(itext):
    vocab = [bytes([i]) for i in range(0, 256)]
    vocab.append("<|endoftext|>".encode("utf-8"))
    # parse
    pre_tokens = [text.encode("utf-8") for text in itext.split()]
    # pretokenization
    pre_tokens = Counter(pre_tokens)
    pre_tokens = [([bytes([b]) for b in i], c) for i, c in pre_tokens.items()]
    # Merges
    for _ in range(0, 7):
        # find the max
        pair_max = defaultdict(int)
        for bts, count in pre_tokens:
            pairs = list(zip(bts, bts[1:]))
            for p in pairs:
                pair_max[p[0] + p[1]] += count
        mval = max(pair_max.values())
        max_keys = [k for k, v in pair_max.items() if v == mval]
        max_key = max(max_keys)
        # merge tokens in pre_tokens
        for i, d in enumerate(pre_tokens):
            for j in range(0, len(d[0]) - 1):
                if j + 1 >= len(d[0]):
                    continue
                if d[0][j] + d[0][j + 1] == max_key:
                    pre_tokens[i][0][j : j + 2] = [
                        pre_tokens[i][0][j] + pre_tokens[i][0][j + 1]
                    ]

    return pre_tokens
    return vocab


print(bpe_example(train_text))
