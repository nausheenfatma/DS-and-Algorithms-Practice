hash_table = [[] for _ in range(10)]
#print (hash_table)


def hashing_func(key):
    return key % len(hash_table)
 
#print (hashing_func(10)) # Output: 0
#print (hashing_func(20)) # Output: 0
#print (hashing_func(25)) # Output: 5

	
def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key].append(value)
 
#insert(hash_table, 10, 'Nepal')
#print (hash_table)

def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists: #if key exists replace value
        bucket[i] = ((key, value))
    else: #add new key, value
        bucket.append((key, value))
 
 
insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print (hash_table)


def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    bucket = hash_table[hash_key]
    for (k,v) in bucket:
        if key == k:
            return v


print (search(hash_table, 10)) # Output: Nepal
print (search(hash_table, 20)) # Output: India
print (search(hash_table, 30)) # Output: None
