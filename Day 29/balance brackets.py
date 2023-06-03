s = input()
st = []
n = len(s)

for i in range(n):
    st.append(s[i])

count = 0
i = 0

while i < n:
    if s[i] == ')':
        st.pop()
    else:
        while st and i < n and s[i] == '(':
            st.pop()
            i += 1
        if i < n:
            count += 1
    i += 1

print(count)