def find_similar_addresses(address, address_list):
    similar_addresses = [x for x in address_list if x.lower().startswith(address.lower())]
    return similar_addresses

address_to_find = input("Enter address to find: ")
address_list =[' 123 Motihari','234 Delhi', '123 Motihari', '55 Bengal']
similar_addresses = find_similar_addresses(address_to_find, address_list)
print("Similar_ADDRESS : ", similar_addresses)