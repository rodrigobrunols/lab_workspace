class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i: int):
        """
        Encontra o representante (raiz) do conjunto ao qual o elemento 'i' pertence.
        Implementa a otimização de Compressão de Caminho.
        """
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, i, j):
        """
        Une os conjuntos que contêm os elementos 'i' e 'j'. Implementa a otimização de União por Rank.
        Retorna True se a união foi realizada, False se já estavam no mesmo conjunto.
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1

            return True

        return False


# Criamos 5 elementos (índices 0 a 4), cada um em seu próprio conjunto.
uf = UnionFind(5)
print(f"Estado Inicial: {uf.parent}")  # [0, 1, 2, 3, 4]

# 1. União (Union): Une 0 e 2
uf.union(0, 2)
# Agora 0 e 2 estão no mesmo conjunto.
# Dependendo dos ranks, a raiz de um aponta para o outro.
print(f"Após Union(0, 2): {uf.parent}")  # Ex: [0, 1, 0, 3, 4] ou [2, 1, 2, 3, 4]

# 2. União: Une 3 e 4
uf.union(3, 4)
print(f"Após Union(3, 4): {uf.parent}")

# 3. Find: Verifica se 0 e 4 estão no mesmo conjunto.
print(f"Raiz de 0: {uf.find(0)}")
print(f"Raiz de 4: {uf.find(4)}")

# 4. União: Une 0 e 4 (unindo os dois grandes conjuntos)
uf.union(0, 4)
print(f"Após Union(0, 4): {uf.parent}")

# 5. Find (Compressão de Caminho): Busca novamente a raiz de 2
# A chamada a find(2) agora fará com que o pai de 2 aponte diretamente
# para a raiz final do grande conjunto {0, 2, 3, 4}.
print(f"Raiz de 2 (com Compressão): {uf.find(2)}")
print(f"Estado após Find(2) (compressão de caminho): {uf.parent}")
