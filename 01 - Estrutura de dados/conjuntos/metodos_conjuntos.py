# {}.union

conjunto_a = {1,2}
conjunto_b = {2,3,4}

# {}.intersection

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.intersection(conjunto_b) # {2,3}

# {}.difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

# {}.symmetric_difference

conjunto_a = {1,2,3} 
conjunto_b = {2,3,4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}


# {}.issubset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False

# {}.issuperset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True

# {}.isdisjoint

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False

# {}.add

sorteio = {1, 25}

sorteio.add(23) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

# {}.clear

sorteio = {1, 25}
sorteio.clear()
sorteio # {}


# {}.copy

sorteio = {1, 25}
sorteio.copy()
sorteio # {1, 25}


# {}.discard

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros # {1,2,3,4,5,6,7,8,9,0}
numeros.discard(1) # {2,3,4,5,6,7,8,9,0}
numeros.discard(45) # {2,3,4,5,6,7,8,9,0}


# {}.pop

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros # {1,2,3,4,5,6,7,8,9,0}
numeros.pop() # {0}
numeros.pop() # {1}
numeros # {2,3,4,5,6,7,8,9}

# {}.remove

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros # {1,2,3,4,5,6,7,8,9,0}
numeros.remove(0)
numeros.remove(45) # KeyError : Element inexistent
numeros # {1,2,3,4,5,6,7,8,9}

# {}.len

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
len(numeros) # 10

# in

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

1 in numeros # True
10 in numeros # False





