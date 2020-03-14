numbers = "1234567890"
other = " !@#$%^&*()_-+=/?.,<>~"
lower_to_number = "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe"
upper_to_number = "5Q7W6E4R2T5Y8U0I9O7P6A4S3D6F8G7H4J2K3L6Z4X9C8V6B5N1M"


class ehash():
    def __init__(self, ehash):
        self.ehash = ehash
        # print(self.final())


    def my_hash(self):
        new_hash = []
        for long in range(len(self.ehash)):
            if self.ehash[long].isupper():
                pass
            elif self.ehash[long].islower():
                pass
            elif self.ehash[long] in other:
                pass
            elif self.ehash[long] in numbers:
                pass
            else:
                print("cant")
                exit()

        for long in range(len(self.ehash)):
            if self.ehash[long].isupper():
                new_hash.append(self.ehash[long].lower())
            elif self.ehash[long].islower():
                new_hash.append(self.ehash[long].upper())
            elif self.ehash[long] in numbers:
                new_hash.append(str(int(self.ehash[long]) + 1))
            elif self.ehash[long] in other:
                place = other.index(self.ehash[long])
                new_hash.append(other[place + 1])

        return "".join(new_hash)


    def part2(self, the_hash):
        new_hash = the_hash[::-1]
        together = []
        for i in range(len(the_hash)):
            together.append(tuple(zip(the_hash, new_hash))[i][0])
            together.append(tuple(zip(the_hash, new_hash))[i][1])
        del together[len(the_hash)]
        together.pop()
        try:
            del together[2]
            del together[5]
            del together[8]
            del together[12]
        except:
            pass

        return "".join(together)


    def part3(self, the_hash):
        new_hash = []
        for e in range(len(the_hash)):
            if the_hash[e] in numbers:
                v = e % 3
                new_hash.append(str(int(the_hash[e]) + v))
            elif the_hash[e] in other:
                place = other.index(the_hash[e])
                new_hash.append(other[place + 1])
            elif the_hash[e] in lower_to_number:
                place = lower_to_number.index(the_hash[e])
                new_hash.append(lower_to_number[place + 1])
            elif the_hash[e] in upper_to_number:
                place = lower_to_number.index(the_hash[e])
                new_hash.append(lower_to_number[place + 1])
        try:
            del new_hash[0]
            del new_hash[1]
            del new_hash[8]
            del new_hash[12]
        except:

            pass

        return "".join(new_hash)[::-1] + "".join(new_hash)


    def part4(self, the_hash):
        new_hash = []
        for i in range(len(the_hash)):
            if i % 1:
                new_hash.append(the_hash[i])
            else:
                pass
        my_list = "qwertyuiopasdf1234ghjklzxcvbnm&*()_+~:{}><?/.,1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+~:{}><?/.,"
        list_of_list = []
        if len(the_hash) > len(my_list):
            return "too long hash"
        for i in range(len(the_hash)):
            y = list_of_list.count(the_hash[i])
            loc = my_list.index(the_hash[i])
            newloc = loc + i
            list_of_list.append(my_list[newloc])
        return "".join(list_of_list)

    # def hash(self):
    #     print(ehash.part4(ehash.part3(ehash.part2(ehash.my_hash()))))

    def __call__(self, m):
        self.ehash = m
        return ehash.part4(ehash.part3(ehash.part2(ehash.my_hash())))


ehash = ehash(None)

# print(ehash("e2we3q3"))
