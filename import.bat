neo4j-admin import ^
--id-type=STRING ^
--database=hygx.db ^
--ignore-duplicate-nodes=true ^
--nodes:Student="Student.csv" ^
--nodes:Book="Book.csv" ^
--nodes:School="School_entity.csv" ^
--relationships:Borrow="Borrow.csv" ^
--relationships:School="School_rel.csv"