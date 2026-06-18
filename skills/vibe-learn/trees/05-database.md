# 05 — 数据库

> 存储数据，查询数据，别丢数据

## 技能点列表

- **数据库是什么**：系统化存储数据的地方。比存文件快、安全、能查。关键词: 数据库, database, 存数据
- **关系型 vs 非关系型怎么选**：数据有明确结构(用户/订单)→关系型(PostgreSQL)；数据结构多变(日志/配置)→非关系型(MongoDB)；缓存/临时数据→Redis。关键词: SQL, NoSQL, 关系型, 非关系型, 选数据库
- **常见数据库一览**：PostgreSQL(最推荐的开源关系型)、MySQL(老牌)、SQLite(本地开发)、MongoDB(文档型)、Redis(缓存/队列)。关键词: PostgreSQL, MySQL, SQLite, MongoDB, Redis
- **表/行/列直观理解**：表=Excel工作表，行=一条记录(一个用户)，列=字段(用户名/邮箱/密码)。关键词: 表, table, 行, row, 列, column
- **主键(PK)与外键(FK)**：主键=每条记录的唯一ID；外键=指向另一张表的关联字段。关键词: primary key, foreign key, 主键, 外键, 关联
- **索引是什么**：给数据库常用查询加目录。不加索引全表扫描=翻整本书找一句话。关键词: index, 索引, 查询慢, 优化
- **SQL基础**：SELECT查、INSERT增、UPDATE改、DELETE删、WHERE条件、ORDER排序、LIMIT限制条数。关键词: SQL, SELECT, INSERT, UPDATE, DELETE, WHERE
- **JOIN是什么**：把两张关联表连在一起查。INNER JOIN(交集)、LEFT JOIN(左边全保留)。关键词: JOIN, INNER JOIN, LEFT JOIN, 多表查询
- **事务(Transaction)**：一组操作要么全成功要么全回滚。转账：A扣钱和B加钱必须同时完成。关键词: transaction, 事务, 回滚, rollback
- **ACID直觉**：原子性(不可分割)、一致性(规则不破坏)、隔离性(并发互不干扰)、持久性(存了不会丢)。关键词: ACID, 原子性, 一致性, 事务特性
- **表设计基本直觉**：每列只存一个值、不要重复存相同数据(用外键引用)、主键用自增ID或UUID。关键词: 表设计, 范式, 数据库设计
- **一对一/一对多/多对多**：用户→手机号(一对一)、用户→订单(一对多)、学生→课程(多对多，需中间表)。关键词: 关系, 一对多, 多对多
- **ORM是什么**：用写代码的方式操作数据库，不用写SQL。Prisma(Node.js)、Drizzle(轻量)、SQLAlchemy(Python)。关键词: ORM, Prisma, Drizzle, SQLAlchemy, TypeORM
- **Migration(数据库迁移)**：用代码定义表结构变更，自动同步到数据库。关键词: migration, 数据库迁移, schema变更
- **Seed(种子数据)**：预置测试数据。方便新开发者一跑就有数据可用。关键词: seed, 种子数据, 测试数据
- **连接池(Connection Pool)**：预建一组数据库连接复用，省去每次请求都新建连接的开销。关键词: connection pool, 连接池
- **常见查询优化**：加索引、避免SELECT *、大数据量分页用游标。关键词: 查询优化, 慢查询, explain
- **Redis缓存概念**：把常用数据放内存里，读取极快。用做Session存储、接口缓存、消息队列。关键词: Redis, 缓存, cache, 内存
- **数据库备份**：定期导出数据库（pg_dump/mysqldump），存到安全位置(不是同一台服务器)。关键词: 备份, pg_dump, dump, 数据库备份
