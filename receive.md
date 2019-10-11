
### 动态编程语言  

原本在编译时执行的操作，可以在运行时完成。即有更长的作用时间和灵活度。  
JS可以在程序运行时 改变 变量的类型，增加新的属性和方法； 

分号：可以不写，但推荐写上；  
当两句行在同一行时，需要写上；  

注释：// 与 /* */


```javascript
/* 这是注释 */
```

### 变量
var 变量名


```javascript
var abc =10; abc
```




    10




```javascript
var _a = 20; _a
```




    20




```javascript
var $e = 'hello'; $e
```




    'hello'




```javascript
var 2a = 30 //不可用数字开头，只能字母，_, $
```


    evalmachine.<anonymous>:1

    var 2a = 30

        ^

    

    SyntaxError: Invalid or unexpected token

        at new Script (vm.js:83:7)

        at createScript (vm.js:265:10)

        at Object.runInThisContext (vm.js:313:10)

        at run ([eval]:1002:15)

        at onRunRequest ([eval]:829:18)

        at onMessage ([eval]:789:13)

        at process.emit (events.js:196:13)

        at emit (internal/child_process.js:860:12)

        at processTicksAndRejections (internal/process/task_queues.js:84:9)


### 非声明变量

1，作用域是全局的。  
2，只有执行赋值操作时才创建；   
3，声明变量是它所在上下文环境的不可配置属性，非声明变量是可配置的可被删除


```javascript
f = 40 ; f //声明变量的作用域限制在其声明位置的上下文中，而非声明变量总是全局的。
```




    40




```javascript
g //必须立刻赋值
```


    evalmachine.<anonymous>:1

    g //必须立刻赋值

    ^

    

    ReferenceError: g is not defined

        at evalmachine.<anonymous>:1:1

        at Script.runInThisContext (vm.js:123:20)

        at Object.runInThisContext (vm.js:313:38)

        at run ([eval]:1002:15)

        at onRunRequest ([eval]:829:18)

        at onMessage ([eval]:789:13)

        at process.emit (events.js:196:13)

        at emit (internal/child_process.js:860:12)

        at processTicksAndRejections (internal/process/task_queues.js:84:9)



```javascript
F = 50; f === F; //区分大小写
```




    false




```javascript
var g = 60 ,g; //逗号操作符，从左到右操作，返回最后结果， undefined
```


```javascript
typeof g
```




    'number'




```javascript
g
```




    60




```javascript
var h = 70, typeof h;
```


    evalmachine.<anonymous>:1

    var h = 70, typeof h;

                ^^^^^^

    

    SyntaxError: Unexpected token typeof

        at new Script (vm.js:83:7)

        at createScript (vm.js:265:10)

        at Object.runInThisContext (vm.js:313:10)

        at run ([eval]:1002:15)

        at onRunRequest ([eval]:829:18)

        at onMessage ([eval]:789:13)

        at process.emit (events.js:196:13)

        at emit (internal/child_process.js:860:12)

        at processTicksAndRejections (internal/process/task_queues.js:84:9)



```javascript
var x = y, y = 'A';
console.log(x + y);

/* 
1, x, y undefined;
2，x = undefined; y = 'A';
3, x + y;
*/
```

    AA



```javascript
var i = 80,
    i; // undefined;
```


```javascript
var i = 80
i;
```




    80




```javascript
i = "hello"; i; //可以改变变量类型。
```




    'hello'




```javascript
i = function(){console.log(1);};i;
```




    [Function: i]




```javascript
i();
```

    1


### 值类型与引用类型


```javascript
var a = 100  //值类型，两块内存空间
var b = a 
a = 200
console.log(b)
```

    100



```javascript
var a = {age:20} //引用类型，变量指向同一内存空间
var b = a
b.age = 21
console.log(a.age)
```

    21


###  引用类型：对象，数组，函数

引用类型：方便共用内存空间，无限制拓展属性，
函数与数组都可以有属性。

#### 函数


```javascript
function fn(){}
fn
```




    [Function: fn]




```javascript
fn.myname = 'myfunction'
fn
```




    [Function: fn] { myname: 'myfunction' }




```javascript
var fn1 = fn
fn1.myname
```




    'myfunction'




```javascript
fn1
```




    [Function: fn] { myname: 'myfunction' }




```javascript
fn1.name; //name 是函数的自带属性；
```




    'fn'



### 数组


```javascript
var myarr = new Array(1,2,3);myarr;
```




    [ 1, 2, 3 ]




```javascript
var myarr2 = [1,2,3];myarr2;
```




    [ 1, 2, 3 ]




```javascript
myarr === myarr2 //指向相同的数组才相等；
```




    false




```javascript
myarr == myarr2 //同上；
```




    false




```javascript
myarr[3] = 4;myarr;
```




    [ 1, 2, 3, 4 ]




```javascript
myarr[6] = 'six'; myarr; //可以空格插入，可以不同类型； 
```




    [ 1, 2, 3, 4, <2 empty items>, 'six' ]




```javascript
myarr.length;
```




    7




```javascript
myarr.length = 10; myarr; //可改变长度，并自行添加空元素
```




    [ 1, 2, 3, 4, <2 empty items>, 'six', <3 empty items> ]




```javascript
typeof myarr[9]; //添加元素为undefined;s
```




    'undefined'




```javascript
arr.name = 'array' // 数组也可以添加属性
arr
```




    [ 1, 2, 3, name: 'array' ]



## typeof


```javascript
typeof c
```




    'undefined'




```javascript
typeof 'abc'
```




    'string'




```javascript
typeof 123
```




    'number'




```javascript
typeof true
```




    'boolean'




```javascript
typeof {}
```




    'object'




```javascript
typeof []
```




    'object'




```javascript
typeof [1,2,3];
```




    'object'




```javascript
typeof null //引用类型，指向空
```




    'object'




```javascript
typeof console.log
```




    'function'



typeof 一共6种类型
只能区分值类型的详细类型，

引用类型是object和 function

null 也是引用类型

## 变量计算

针对值类型计算：
* 字符串拼接
* == 运算符 ,在判断对象属性、参数是否存在时。==就是多种===情况取或时的简化
* if
* 逻辑运算


```javascript
var a = 100+10
a
```




    110




```javascript
var b = 100+'10'
b
```




    '10010'




```javascript
100 == '100'
```




    true




```javascript
0 == '' //转为false
```




    true




```javascript
null == undefined 
```




    true



if 判断时会执行强制类型转换


```javascript
console.log(10 && 0)
```

    0



```javascript
console.log(''||'abc')
```

    abc



```javascript
console.log(' '||'abc')
```

     



```javascript
console.log(!window.abc) //浏览器执行为true
```


    evalmachine.<anonymous>:1

    console.log(!window.abc) //浏览器执行为true

                 ^

    

    ReferenceError: window is not defined

        at evalmachine.<anonymous>:1:14

        at Script.runInThisContext (vm.js:123:20)

        at Object.runInThisContext (vm.js:313:38)

        at run ([eval]:1002:15)

        at onRunRequest ([eval]:829:18)

        at onMessage ([eval]:789:13)

        at process.emit (events.js:196:13)

        at emit (internal/child_process.js:860:12)

        at processTicksAndRejections (internal/process/task_queues.js:84:9)



```javascript
var a = 100
console.log(!!a) //把变量转换为true or false
```

    true



```javascript
!!0
```




    false




```javascript
!!NaN
```




    false




```javascript
!!''
```




    false




```javascript
!!' ' //空格强转为true
```




    true




```javascript
!!null
```




    false




```javascript
!!undefined
```




    false




```javascript
!!false
```




    false



### JSON 是个JS对象，同Math
有两个api, 
同时也是一种数据格式.

### 内置函数


```javascript
Object
```




    [Function: Object]




```javascript
Array
```




    [Function: Array]




```javascript
Function
```




    [Function: Function]



### 内置对象


```javascript
Math
```




    Object [Math] {}




```javascript
JSON
```




    Object [JSON] {}


