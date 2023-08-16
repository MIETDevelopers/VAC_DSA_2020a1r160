# Return method.
def details(**args):
    for i, value, in args.items():
        return {i:value}
print(details(Name="Ishav Vemra", RollNumber="2020a1r160"))