## Blog

### 前言

这个blog是在上一个blog的基础优化，更新。大概前段界面，后端增加新功能。

---

### 环境

- Django 2.1.5
- Bootstrap 4
- Mysql 5.6以上 (可选)

---

### 运行

```python
python manage.py makemigrations
python manage.py migrate
python runserver
```

---

### 初始化

- 导航栏
  - 导航栏是在数据库中添加的，需要填三个参数
    - 标题
    - [Font-Awesome](https://fontawesome.com/icons)
    - 路由
    - ![1568311329003](\md_img\1568311329003.png)
  - 默认5个
  - 可修改填加路由，前提是你自己加上
- Classify页面的button颜色，需在后端添加，默认7 种颜色，具体可参考[Buttons](https://www.bootcss.com/p/buttons/)

