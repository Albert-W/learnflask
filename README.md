# learn flask 

### Install flask
```bash
pip install Flask
```
Different methods to pass parameters through Flask

| Input Parameter                                           | Get Parameter                                                              |
|-----------------------------------------------------------|----------------------------------------------------------------------------|
| url <br> ({{url}}/user/456)                                     | /user/<int:user_id> <br> 456                                                     |
| Query Params <br> ({{url}}/join?id=id4)                         | request.args.get('id','') <br> id4                                               |
| Body form-data && <br> x-www-form-urlencoded <br> key = id <br> value = id2 | request.form['id'] <br> id2                                                      |
| Body raw <br> raw data                                          | request.data <br> b"raw data"                                                    |
| Body form-data file <br> key = file <br> value=test.txt               | data = request.files.get('file') <br> data.save('receive.txt')                   |
| Body binary                                               | data = request.get_data() <br> f = open('receive.md','wb') <br> f.write(data) <br> f.close() |



