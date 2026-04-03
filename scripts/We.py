'''
Author: ka1shu1 cwh979946@163.com
Date: 2026-04-02 16:16:22
LastEditors: ka1shu1 cwh979946@163.com
LastEditTime: 2026-04-02 16:39:48
FilePath: \AICAD_Research\scripts\We.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import gensim.downloader

model = gensim.downloader.load("glove-wiki-gigaword-50")

model["tower"]