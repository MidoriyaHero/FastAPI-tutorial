# Lecture 2: Path Parameters

READ THIS [LINK](https://fastapi.tiangolo.com/tutorial/path-params/) to learn about the basic concept

### Here I will give you somethings that I noted:

```
You should declare the type of a path parameter in the function (int, str, ect)
```

```
Remember to create a FIXED PATH above DYNAMIC PATH (user/me above user/{user_id})

bc fastapi code run top to bottom. So, if dynamic path is above fixed path, 

then the first one will always be used since the path matches first

Similarly, you cannot redefine a path operation
```

## USE THIS COMMAND TO START APP SERVER:
```
cd Lecture 2
uvicorn main:app --reload
```