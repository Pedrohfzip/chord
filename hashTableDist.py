class TabelaHashDistribuida:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets  # Número de buckets na tabela hash
        self.buckets = [[] for _ in range(num_buckets)]  # Lista de listas para armazenar os elementos

    def funcao_hash(self, chave):
        return hash(chave) % self.num_buckets  # Função de hash para determinar o índice do bucket

    def inserir(self, chave, valor):
        valor_hash = self.funcao_hash(chave)  # Calcula o índice do bucket usando a função de hash
        bucket = self.buckets[valor_hash]  # Obtém o bucket correspondente
        for i, (chave_existente, _) in enumerate(bucket):
            if chave_existente == chave:
                bucket[i] = (chave, valor)  # Atualiza o valor se a chave já existir
                return
        bucket.append((chave, valor))  # Adiciona um novo par chave-valor ao bucket

    def obter(self, chave):
        valor_hash = self.funcao_hash(chave)  # Calcula o índice do bucket usando a função de hash
        bucket = self.buckets[valor_hash]  # Obtém o bucket correspondente
        for chave_existente, valor in bucket:
            if chave_existente == chave:
                return valor  # Retorna o valor correspondente à chave, se existir
        return None  # Retorna None se a chave não for encontrada

    def remover(self, chave):
        valor_hash = self.funcao_hash(chave)  # Calcula o índice do bucket usando a função de hash
        bucket = self.buckets[valor_hash]  # Obtém o bucket correspondente
        for i, (chave_existente, _) in enumerate(bucket):
            if chave_existente == chave:
                del bucket[i]  # Remove o par chave-valor do bucket
                return
        raise KeyError("Chave não encontrada na tabela hash.")  # Levanta uma exceção se a chave não for encontrada

if __name__ == "__main__":
    dht = TabelaHashDistribuida(num_buckets=15)
    dht.inserir("apple", 5)
    dht.inserir("apple2", 5)
    dht.inserir("apple3", 5)
    dht.inserir("apple4", 5)
    dht.inserir("banana", 7)
    dht.inserir("orange", 3)
    dht.inserir("grape", 9)

    print(dht.obter("apple2"))
    