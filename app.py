from pytube import YouTube

yt = YouTube(input("Digite a ulr do video que deseja baixar: "))

print(yt.title)
desc = yt.description
if yt.description:
    print(desc)

else:
    print("Descrição indisponível")