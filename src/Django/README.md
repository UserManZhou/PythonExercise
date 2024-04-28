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
