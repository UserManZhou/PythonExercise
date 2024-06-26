# 1.什么是Django?

1. Django 最初被设计用于具有快速开发需求的新闻类站点，目的是要实现简单快捷的网站开发。以下内容简要介绍了如何使用 Django
   实现一个数据库驱动的网络应用。
2. 为了让您充分理解 Django 的工作原理，这份文档为您详细描述了相关的技术细节，不过这并不是一份入门教程或者是参考文档（我们当然也为您准备了这些）。如果您想要马上开始一个项目，可以从
   实例教程 开始入手，或者直接开始阅读详细的 参考文档。

# 2.快速安装指南

1. 开始用 Django
   前，需要先进行安装。我们写了 [完整安装指南](https://docs.djangoproject.com/zh-hans/5.0/topics/install/ "完整安装指南")
   罗列了各种安装方法和情况；它会指导你完成一个简易安装，只要你按照指示操作，就可以运行得起来。

## 2.1 安装python

1. Django 是一个用于 Python
   的网络框架。有关详细信息，请参阅 [我应该使用哪个版本的 Python 来配合 Django?](https://docs.djangoproject.com/zh-hans/5.0/faq/install/#faq-python-version-support)。
2. 可以通过 https://www.python.org/downloads/ 或者操作系统的包管理工具获取最新版本的 Python。

## 2.2 安装Apache和mod_wsgi

1. 如果您想在生产站点上使用 Django，请使用 [Apache](https://httpd.apache.org/)
   与 [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/)。mod_wsgi 有两种模式：嵌入模式和守护模式。在嵌入模式下，mod_wsgi
   类似于 mod_perl -- 它将 Python 嵌入到 Apache 中，并在服务器启动时将 Python 代码加载到内存中。代码在整个 Apache
   进程的生命周期内保持在内存中，这会比其他服务器配置方式带来显著的性能提升。在守护模式下，mod_wsgi
   会生成一个独立的守护进程来处理请求。守护进程可以以与 Web 服务器不同的用户身份运行，从而可能提高安全性。守护进程可以在不重新启动整个
   Apache Web 服务器的情况下重新启动，从而可能使代码库的刷新更加无缝。请参考 mod_wsgi 文档以确定哪种模式适合您的设置。确保已安装
   Apache 并启用了 mod_wsgi 模块。Django 将与支持 mod_wsgi 的任何版本的 Apache 配合使用。

## 2.3 安装pip（Python 的包安装程序）/通过 pip 安装正式发布版本

1. https://pip.pypa.io/en/stable/
1. 以下是安装 Django 的推荐方式。
    1. 安装 [pip](https://pip.pypa.io/en/stable/)。最简单的方式是使用 独立 [pip 安装器](https://pip.pypa.io/en/stable/)
       。若你的系统早已安装 **pip**，你可能需要更新它，因为它可能过期了。如果它过期了，你会知道的，因为过期的用不了。
    2. 看一下 [venv](https://docs.python.org/3/tutorial/venv.html)
       。这个工具提供了隔离的Python环境，比在系统内安装包更实用。它还允许在没有管理员权限的情况下安装包。贡献指南
       介绍了如何创建一个虚拟环境。
    3. 在你已创建并激活一个虚拟环境后，输入以下命令: `$ python -m pip install Django`

# 3.安装开发版本

1. 如果你希望偶尔能获取最新的补丁和改进，遵循以下说明
    2. 确保你已安装了 Git，这样你就可以从 shell 运行对应命令。（在 shell 中输入 git help 测试是否安装。）
    3. 像这样检出 Django 的主开发分支：`$ git clone https://github.com/django/django.git` 这会在当前目录创建一个 django
       目录。
    4. 确保 Python 解释器可以加载 Django 的代码。最方便的方法是使用虚拟环境和 pip。 贡献指南 简略介绍了如何创建虚拟环境。
    5. 设置并激活虚拟环境后，运行以下命令：`$ python -m pip install -e django/`
    6. 这会让 Django 的代码可导入，使得 django-admin 命令行工具可用。换句话说，大事可为。
    7. 当你想更新你的 Django 源代码时，在 django 目录下运行 git pull 命令。当你这样做的时候，Git 会下载所有变更。

# 4.验证Django的安装

1. 若要验证 Django 是否能被 Python 识别，可以在 shell 中输入 **python**。 然后在 Python 提示符下，尝试导入 Django：
   `>>> import django `
   `>>> print(django.get_version())`

# 5.创建项目

1. 如果这是你第一次使用 Django 的话，你需要一些初始化设置。也就是说，你需要用一些自动生成的代码配置一个 Django project ——
   即一个 Django 项目实例需要的设置项集合，包括数据库配置、Django 配置和应用程序配置。
2. 打开命令行，cd 到一个你想放置你代码的目录，然后运行以下命令： `$ django-admin startproject mysite`
3. 这行代码将会在当前目录下创建一个 **mysite** 目录。如果命令失败了，查看 运行 django-admin 时遇到的问题，可能能给你提供帮助。
4. 备注:**你得避免使用 Python 或 Django 的内部保留字来命名你的项目。具体地说，你得避免使用像 django (会和 Django
   自己产生冲突)或 test (会和 Python 的内置组件产生冲突)这样的名字。**
5. 我的代码该放在哪？
    1. 如果你的背景是普通的老式 PHP（没有使用过现代框架），你可能习惯于把代码放在网络服务器的文档根目录下（比如 /var/www ）。在
       Django 中，你不需要这样做。把任何 Python 代码放在网络服务器的文档根目录下都不是一个好主意，因为这有可能使人们能够通过网络查看你的代码。这对安全没有好处。
    2. 把你的代码放在文档根目录 以外 的某些地方吧，比如 /home/mycode。

# 6.项目生成目录结构 

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

1. 这些目录和文件的用处是：
    - 外层的 **mysite/** 根目录只是你项目的容器， 根目录名称对 **Django** 没有影响，你可以将它重命名为任何你喜欢的名称。
    - **manage.py**: 一个让你用各种方式管理 **Django**
      项目的命令行工具。你可以阅读 [django-admin 和 manage.py](https://docs.djangoproject.com/zh-hans/5.0/ref/django-admin/)
      获取所有 **manage.py**
      的细节。
    - 里面一层的 **mysite/** 目录包含你的项目，它是一个纯 **Python** 包。它的名字就是当你引用它内部任何东西时需要用到的 *
      *Python** 包名。 (比如 **mysite.urls**).
    - **mysite/__init__.py**：一个空文件，告诉 **Python** 这个目录应该被认为是一个 **Python** 包。如果你是 **Python**
      初学者，阅读官方文档中的 [更多关于包的知识](https://docs.python.org/3/tutorial/modules.html#tut-packages)。
    - **mysite/settings.py**：**Django**
      项目的配置文件。如果你想知道这个文件是如何工作的，请查看 [Django 配置](https://docs.djangoproject.com/zh-hans/5.0/topics/settings/)
      了解细节。
    - **mysite/urls.py**：**Django** 项目的 URL
      声明，就像你网站的“目录”。阅读 [URL调度器](https://docs.djangoproject.com/zh-hans/5.0/topics/http/urls/) 文档来获取更多关于
      **URL** 的内容。
    - **mysite/asgi.py**：作为你的项目的运行在 ASGI 兼容的 Web
      服务器上的入口。阅读 [如何使用 ASGI 来部署](https://docs.djangoproject.com/zh-hans/5.0/howto/deployment/asgi/)
      了解更多细节。
    - **mysite/wsgi.py**：作为你的项目的运行在 WSGI
      兼容的Web服务器上的入口。[阅读 如何使用 WSGI 进行部署 了解更多细节](https://docs.djangoproject.com/zh-hans/5.0/howto/deployment/wsgi/)。

# 7.运行项目

1. 让我们来确认一下你的 Django 项目是否真的创建成功了。如果你的当前目录不是外层的 mysite 目录的话，请切换到此目录，然后运行下面的命令：
   `$ python manage.py runserver`
2. 你应该会看到如下输出：
   `Performing system checks... System check identified no issues (0 silenced). You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.
   四月 26, 2024 - 15:50:53
   Django version 5.0, using settings 'mysite.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.`
3. 更换端口：`$ python manage.py runserver 8080`
4. 更换服务ip:`$ python manage.py runserver 0.0.0.0:8000`
5. 会自动重新加载的服务器 **runserver**:用于开发的服务器在需要的情况下会对每一次的访问请求重新载入一遍 Python
   代码。所以你不需要为了让修改的代码生效而频繁的重新启动服务器。然而，一些动作，比如添加新文件，将不会触发自动重新加载，这时你得自己手动重启服务器。

# 8.创建应用

1. 请确定你现在处于 **manage.py** 所在的目录下，然后运行这行命令来创建一个应用：`$ python manage.py startapp polls`
2. 这将创建一个名为 polls 的目录，其布局如下：

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

3. 这个目录结构包括了投票应用的全部内容。

## 8.1 编写第一个视图

1. 让我们开始编写第一个视图吧。打开 **polls/views.py**，把下面这些 Python 代码输入进去：

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

2. 这是 Django 中最简单的视图。如果想看见效果，我们需要将一个 URL 映射到它——这就是我们需要 URLconf 的原因了。要在 polls
   目录中创建一个 URL 配置，请创建一个名为 **urls.py** 的文件。现在你的应用程序目录应该如下所示：

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

3. 在 **polls/urls.py** 中，输入如下代码：

```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

4. 下一步是要在根 **URLconf** 文件中指定我们创建的 **polls.urls** 模块。在 **mysite/urls.py** 文件的 **urlpatterns**
   列表里插入一个 **include()**， 如下：

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

5. 函数 **include()** 允许引用其它 **URLconfs**。每当 **Django** 遇到 **include()** 时，它会截断与此项匹配的 URL
   的部分，并将剩余的字符串发送到**URLconf** 以供进一步处理。我们设计 **include()** 的理念是使其可以即插即用。因为投票应用有它自己的
   **URLconf( polls/urls.py )**，他们能够被放在 "/polls/" ， "/fun_polls/" ，"/content/polls/"，或者其他任何路径下，这个应用都能够正常工作。
6. 你现在把 **index** 视图添加进了 URLconf。通过以下命令验证是否正常工作：

```
$ python manage.py runserver
```

7. 用你的浏览器访问 http://localhost:8000/polls/, 你应该能够看见 "Hello, world. You're at the polls index." ，这是你在
   **index** 视图中定义的。

# 9.创建应用（二）

> 本教程从 教程1 结束的地方开始。我们将设置数据库，创建第一个模型，并快速介绍 Django 自动生成的后台界面。

## 9.1数据库配置

1. 现在，打开 **mysite/settings.py** 。这是个包含了 Django 项目设置的 Python 模块。
2. 通常，这个配置文件使用 SQLite 作为默认数据库。如果你不熟悉数据库，或者只是想尝试下 Django，这是最简单的选择。Python 内置
   SQLite，所以你无需安装额外东西来使用它。当你开始一个真正的项目时，你可能更倾向使用一个更具扩展性的数据库，例如
   PostgreSQL，避免中途切换数据库这个令人头疼的问题。
3. 如果你想使用其他数据库，你需要安装合适的
   [database bindings](https://docs.djangoproject.com/zh-hans/5.0/topics/install/#database-installation)
   ，然后改变设置文件中 **DATABASES 'default'** 项目中的一些键值：
   1. 下面是一个使用 MySQL 选项文件的配置示例：

```
# settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "/path/to/my.cnf",
        },
    }
}
```

```
# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
```

4. 如果你想使用其他数据库，
   你需要安装合适的 [database bindings](https://docs.djangoproject.com/zh-hans/5.0/topics/install/#database-installation)
   ，然后改变设置文件中 **DATABASES 'default'** 项目中的一些键值
   - [ENGINE](https://docs.djangoproject.com/zh-hans/5.0/ref/settings/#std-setting-DATABASE-ENGINE) - 可选值有
      - **'django.db.backends.sqlite3'，'django.db.backends.postgresql'，'django.db.backends.mysql'，或 '
        django.db.backends.oracle'**
        。其它 [可用后端](https://docs.djangoproject.com/zh-hans/5.0/ref/databases/#third-party-notes)。
      - [NAME](https://docs.djangoproject.com/zh-hans/5.0/ref/settings/#std-setting-NAME) -- 数据库的名称。如果你使用
        SQLite，数据库将是你电脑上的一个文件，在这种情况下，**NAME**
        应该是此文件完整的绝对路径，包括文件名。默认值 **BASE_DIR / 'db.sqlite3'** 将把数据库文件储存在项目的根目录。
5. 如果你不使用 SQLite，则必须添加一些额外设置，比如 **USER 、 PASSWORD 、 HOST** 等等。想了解更多数据库设置方面的内容，请看文档：
   **DATABASES** 。
6. 编辑 **mysite/settings.py**
   文件前，先设置 [TIME_ZONE](https://docs.djangoproject.com/zh-hans/5.0/ref/settings/#std-setting-TIME_ZONE) 为你自己时区。

```
TIME_ZONE = 'Asia/Shanghai'
```

7. 此外，
   关注一下文件头部的 [INSTALLED_APPS](https://docs.djangoproject.com/zh-hans/5.0/ref/settings/#std-setting-INSTALLED_APPS)
   设置项。这里包括了会在你项目中启用的所有 Django
   应用。应用能在多个项目中使用，你也可以打包并且发布应用，让别人使用它们。
   - [django.contrib.admin](https://docs.djangoproject.com/zh-hans/5.0/ref/contrib/admin/#module-django.contrib.admin) -
     管理员站点， 你很快就会使用它。
   - [django.contrib.auth](https://docs.djangoproject.com/zh-hans/5.0/topics/auth/#module-django.contrib.auth) - 认证授权系统。
   - [django.contrib.contenttypes](https://docs.djangoproject.com/zh-hans/5.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes) -
     内容类型框架。
   - [django.contrib.sessions](https://docs.djangoproject.com/zh-hans/5.0/topics/http/sessions/#module-django.contrib.sessions) -
     会话框架。
   - [django.contrib.messages](https://docs.djangoproject.com/zh-hans/5.0/ref/contrib/messages/#module-django.contrib.messages) -
     消息框架。
   - [django.contrib.staticfiles](https://docs.djangoproject.com/zh-hans/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles) -
     管理静态文件的框架。
8. 这些应用被默认启用是为了给常规项目提供方便。
9. 默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。请执行以下命令：

```
$ python manage.py migrate
```

10. 这个 [migrate](https://docs.djangoproject.com/zh-hans/5.0/ref/django-admin/#django-admin-migrate) 命令查看
    [INSTALLED_APPS](https://docs.djangoproject.com/zh-hans/5.0/ref/settings/#std-setting-INSTALLED_APPS) 配置，并根据
    **mysite/settings.py**
    文件中的数据库配置和随应用提供的数据库迁移文件（我们将在后面介绍这些），创建任何必要的数据库表。你会看到它应用的每一个迁移都有一个消息。如果你有兴趣，运行你的数据库的命令行客户端，输入
    **\dt** （PostgreSQL）， **SHOW TABLES**; （MariaDB，MySQL）， **.tables** （SQLite）或 **SELECT TABLE_NAME FROM USER_TABLES;
    ** （Oracle）来显示
    Django 创建的表。

## 9.2 创建模型

1. 在 Django 里写一个数据库驱动的 Web 应用的第一步是定义模型 - 也就是数据库结构设计和附加的其它元数据。

```
设计哲学
1. 一个模型就是单个定义你的数据的信息源。模型中包含了不可缺少的数据区域和你存储数据的行为。Django 遵循 。目的就是定义你的数据模型要在一位置上，而且自动从该位置推导一些事情
2.来介绍一下迁移 - 举个例子，不像 Ruby On Rails，Django 的迁移代码是由你的模型文件自动生成的，它本质上是个历史记录，Django 可以用它来进行数据库的滚动更新，通过这种方式使其能够和当前的模型匹配。
```

2. 在这个投票应用中，需要创建两个模型：问题 **Question** 和选项 **Choice。Question** 模型包括问题描述和发布时间。**Choice**
   模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。
3. 这些概念可以通过一个 Python 类来描述。按照下面的例子来编辑 **polls/models.py** 文件：

```
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

```

4. 每个模型被表示为
   [django.db.models.Model](https://docs.djangoproject.com/zh-hans/5.0/ref/models/instances/#django.db.models.Model)
   类的子类。每个模型有许多类变量，它们都表示模型里的一个数据库字段。
5. 每个字段都是 [Field](https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/#django.db.models.Field) 类的实例 -
   比如，字符字段被表示为 CharField ，日期时间字段被表示为 DateTimeField 。这将告诉
   Django
   每个字段要处理的数据类型。
6. 每个 [Field](https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/#django.db.models.Field) 类实例变量的名字（例如
   **question_text** 或 **pub_date** ）也是字段名，所以最好使用对机器友好的格式。你将会在 Python 代码里使用它们，而数据库会将它们作为列名。
7. 你可以使用可选的选项来为
   [Field](https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/#django.db.models.Field)
   定义一个人类可读的名字。这个功能在很多 Django
   内部组成部分中都被使用了，而且作为文档的一部分。如果某个字段没有提供此名称，Django 将会使用对机器友好的名称，也就是变量名。在上面的例子中，我们只为
   **Question.pub_date** 定义了对人类友好的名字。对于模型内的其它字段，它们的机器友好名也会被作为人类友好名使用。
8. 定义某些 [Field](https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/#django.db.models.Field) 类实例需要参数。例如
   [CharField](https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/#django.db.models.CharField) 需要一个
   [max_length](https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/#django.db.models.CharField.max_length)
   参数。这个参数的用处不止于用来定义数据库结构，也用于验证数据，我们稍后将会看到这方面的内容。
9. [Field](https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/#django.db.models.Field) 也能够接收多个可选参数；在上面的例子中：我们将
   **votes** 的 **default** 也就是默认值，设为0。
10. 注意在最后，
    我们使用 [ForeignKey](https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/#django.db.models.ForeignKey)
    定义了一个关系。这将告诉 Django，每个 Choice 对象都关联到一个 **Question** 对象。**Django**
    支持所有常用的数据库关系：多对一、多对多和一对一。

## 9.3 激活模型

1. 上面的一小段用于创建模型的代码给了 Django 很多信息，通过这些信息，Django 可以：
   - 为这个应用创建数据库 schema（生成 **CREATE TABLE** 语句）。
   - 创建可以与 **Question** 和 **Choice** 对象进行交互的 Python 数据库 API。
     但是首先得把 **polls** 应用安装到我们的项目里。

```
设计哲学

   Django 应用是“可插拔”的。你可以在多个项目中使用同一个应用。除此之外，你还可以发布自己的应用，因为它们并不会被绑定到当前安装的 Django 上。

```

2. 为了在我们的工程中包含这个应用，
   我们需要在配置类 [INSTALLED_APPS](https://docs.djangoproject.com/zh-hans/5.0/ref/settings/#std-setting-INSTALLED_APPS)
   中添加设置。因为 **PollsConfig** 类写在文件 **polls/apps.py**
   中，所以它的点式路径是 **'polls.apps.PollsConfig'**。在文件 **mysite/settings.py**
   中 [INSTALLED_APPS](https://docs.djangoproject.com/zh-hans/5.0/ref/settings/#std-setting-INSTALLED_APPS)
   子项添加点式路径后，它看起来像这样：

```
# Application definition

INSTALLED_APPS = [
    # 添加项目进去
    "polls.apps.PollsConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

3. 现在你的 Django 项目会包含 polls 应用。接着运行下面的命令：
   ` $ python manage.py makemigrations polls `
4. 你将会看到类似于下面这样的输出：

```
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

5. 通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次
   迁移。

6. 迁移是 Django 对于模型定义（也就是你的数据库结构）的变化的储存形式 - 它们其实也只是一些你磁盘上的文件。如果你想的话，你可以阅读一下你模型的迁移数据，它被储存在
   polls/migrations/0001_initial.py 里。别担心，你不需要每次都阅读迁移文件，但是它们被设计成人类可读的形式，这是为了便于你手动调整
   Django 的修改方式。

7. Django 有一个自动执行数据库迁移并同步管理你的数据库结构的命令 -
   这个命令是 [migrate](https://docs.djangoproject.com/zh-hans/5.0/ref/django-admin/#django-admin-migrate)
   ，我们马上就会接触它 -
   但是首先，让我们看看迁移命令会执行哪些 SQL
   语句。[sqlmigrate](https://docs.djangoproject.com/zh-hans/5.0/ref/django-admin/#django-admin-sqlmigrate)
   命令接收一个迁移的名称，然后返回对应的 SQL：

```
$ python manage.py sqlmigrate polls 0001
```

8. 你将会看到类似下面这样的输出（我把输出重组成了人类可读的格式）：

```
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL,
    "question_id" bigint NOT NULL
);
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");

COMMIT;
```

9. 请注意以下几点：

   - 输出的内容和你使用的数据库有关，上面的输出示例使用的是 PostgreSQL。
   - 数据库的表名是由应用名(polls)和模型名的小写形式( question 和 choice)连接而来。（如果需要，你可以自定义此行为。）
   - 主键(IDs)会被自动创建。(当然，你也可以自定义。)
   - 默认的，Django 会在外键字段名后追加字符串 "_id" 。（同样，这也可以自定义。）
   - 外键关系由 FOREIGN KEY 生成。你不用关心 DEFERRABLE 部分，它只是告诉 PostgreSQL，请在事务全都执行完之后再创建外键关系。
   - 它是为你正在使用的数据库定制的，因此特定于数据库的字段类型，例如“auto_increment”（MySQL）、“bigint PRIMARY KEY GENERATED
     BY
   - DEFAULT AS IDENTITY”（PostgreSQL）或“integer primary key autoincrement” `` (SQLite) 会自动为您处理。
   - 字段名称的引用也是如此——例如，使用双引号或单引号。
   - 这个 sqlmigrate 命令并没有真正在你的数据库中的执行迁移 - 相反，它只是把命令输出到屏幕上，让你看看 Django 认为需要执行哪些
   - SQL 语句。这在你想看看 Django 到底准备做什么，或者当你是数据库管理员，需要写脚本来批量处理数据库时会很有用。
   - 如果你感兴趣，你也可以试试运行 python manage.py check ;这个命令帮助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作。

10. 现在，再次运行 migrate 命令，在数据库里创建新定义的模型的数据表：
