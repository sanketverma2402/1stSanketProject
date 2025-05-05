st={"abc",101,55.6,201,201}

print(st)
print(len(st))

print("---add element---")
st.add(5)
st.add("xyz")
print(st)

print("-----Add multiple elements------")
st.update([-1,-5])
print(st)

print("-------Remove Elements------")
# st.remove(-7)      #throws error if the element doesn't exist
st.discard(-5)   #no error even if the element doesn't exist
print(st)

st.pop()       #remove random elememt
print(st)

print("-----copy set-----")
st2=st.copy()
print(st2)

print("-----sorting-----")
st3={5,20,90,1,80,7}
print(st3)
st4=sorted(st3)
print(st4)

print("----clear set----")
st3.clear()
print(len(st3))

print("--delete set---")
del st3
print(st3)

st4={}