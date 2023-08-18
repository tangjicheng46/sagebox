from setuptools import setup, find_packages

def read_version() -> str:
    with open("./sagebox/__init__.py", "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

# 从 requirements.txt 读取依赖项
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='sagebox',
    version=read_version(),
    author='tangjicheng',
    author_email='tangjch15@gmail.com',
    description='Essential tools for programmer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tangjicheng46/sagebox',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='AI, sagebox, python',
    install_requires=required,  # 从requirements.txt添加的依赖
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'remove_pycache=sagebox.scripts.remove_pycache:main',
        ]
    },
)
