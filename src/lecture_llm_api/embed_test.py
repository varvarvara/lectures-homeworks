from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import numpy as np

from scipy.spatial import distance

load_dotenv(find_dotenv())


def get_embeddings(texts: list[str]) -> list[np.array]:
    client = OpenAI()

    embeddings = client.embeddings.create(
        model="Qwen/Qwen3-Embedding-0.6B", input=texts
    )
    numpy_arrays = []
    for emb in embeddings.data:
        numpy_arrays.append(np.array(emb.embedding))
    return numpy_arrays


if __name__ == "__main__":
    sex_embeddings = get_embeddings(
        ["билет мужчины N9913-123asd-dasdad", "билет женщины N9912-dsadasd-23"]
    )
    target_embedding = get_embeddings(["билет N9912"])[0]

    # мужчина
    print("Мужчина")
    print("cosine:", distance.cosine(sex_embeddings[0], target_embedding))
    print("mink=1", distance.minkowski(sex_embeddings[0], target_embedding, p=1))
    print("mink=2", distance.minkowski(sex_embeddings[0], target_embedding, p=2))
    print("mink=2.5", distance.minkowski(sex_embeddings[0], target_embedding, p=2.5))
    print("mink=3", distance.minkowski(sex_embeddings[0], target_embedding, p=3))
    print("mink=4", distance.minkowski(sex_embeddings[0], target_embedding, p=4))

    men = distance.cosine(sex_embeddings[0], target_embedding)

    print("@:", sex_embeddings[0] @ target_embedding.T)
    print()

    # женщина
    print("Женщина")
    print("cosine:", distance.cosine(sex_embeddings[1], target_embedding))
    print("mink=1", distance.minkowski(sex_embeddings[1], target_embedding, p=1))
    print("mink=2", distance.minkowski(sex_embeddings[1], target_embedding, p=2))
    print("mink=2.5", distance.minkowski(sex_embeddings[1], target_embedding, p=2.5))
    print("mink=3", distance.minkowski(sex_embeddings[1], target_embedding, p=3))
    print("mink=4", distance.minkowski(sex_embeddings[1], target_embedding, p=4))
    print("@:", sex_embeddings[1] @ target_embedding.T)

    women = distance.cosine(sex_embeddings[1], target_embedding)

    print()
    if abs(women - men) < 0.02:
        print("ВМЕСТЕ")
    else:
        print("ЖЕНЩИНЫ" if women < men else "МУЖЧИНЫ")
