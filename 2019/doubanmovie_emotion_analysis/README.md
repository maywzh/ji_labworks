# doubanmovie_false_rating

## 爬虫
```bash
cd movie_review
scrapy crawl top #爬取影片id
scrapy crwal topall #爬取影片详细信息
scrapy crawl douban #爬取影评
```

## 训练
```bash
python naive_bayes_train.py
python naive_bayes_test.py
```

## 测试
```bash
python run.py
```

## TO-DO
- 实现影评和简介的相似度判断
- 自动化测试和训练 