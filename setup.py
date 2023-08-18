from setuptools import setup, find_packages

# 从 requirements.txt 读取依赖项
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='sagebox',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Elevate your AI projects with seasoned intelligence.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/sagebox',
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
    keywords='AI tools, sagebox, python',
    install_requires=required,  # 从requirements.txt添加的依赖
    python_requires='>=3.6',
    entry_points={
    },
)
