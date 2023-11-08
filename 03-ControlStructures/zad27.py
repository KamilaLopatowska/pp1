facebook = False
twitter = True
instagram = True

if (facebook and twitter) or (facebook and instagram) or (instagram and twitter):
    print("A person can be a good influencer!")
else:
    print("A person cannot be a good influencer.")