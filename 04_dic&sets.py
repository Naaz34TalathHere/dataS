info={
    "key":"value",
    "name":"John",
    "age":20,
    "city":"New York",
    12.9:29
    }
print(info["name"])
print(info["age"])
print(type(info))
print(info["key"])
info["name"]="naaz"
null_dict={}
print(null_dict)
student={
    "name":"naaz",
    "sub":{
        "phy":45,
        "mat":45,
        
}
}
print(student['sub']['phy'])
print(info.keys())
print(info.values())
print(list(student.keys()))
print(list(info.keys()))
print(info.items())
info.update({"age":23})
print(info.values())

# SETS
set_1={1,2,3,4}
print(type(set_1))
se_2={1,1,2,3,3,'Hello','helllo','hi','hi'}
print(se_2)
print(len(se_2))
null_set=set()
print(null_set)

dic={
    "table":["apiece of furniture","list of factes  fig"],
    "car" :" a small anial"

}
print(dic)
stud={"python",'java','c++','python','javascript','java','python','java','c++','c'
    }
print(len(stud))

dic={}
x=int(input("enter phys:"))
y=int(input("enter chem:"))

z=int(input("enter math:"))
dic.update({"phy":x})
dic.update({"chem":y})
dic.update({"math":z})
print(dic)
val={9,9.0}
print(val)
val={9,'9.0'}
print(val)
vv={("int",9),("float",9.0)
    }
print(vv)