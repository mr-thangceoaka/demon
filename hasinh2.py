n=int(input())
k=int(input())
a=[0]*100
def ktao():
    for i in range(1,k+1):
        a[i]=i
def sinh():
    i=k
    while i>=1 and a[i]==n-k+i:
        i-=1
    if i==0:
        return False
    else:
        a[i]+=1
        for j in range(1,k+1):
            a[j]=a[j-1]+1
def main():
    ok = True
    ktao()
    while ok:
        for i in range(1, n + 1):
            print(a[i], end='')
        print()
        ok = sinh()  # Gọi hàm sinh để cập nhật biến ok

if __name__ == "__main__":
    main()
          
    