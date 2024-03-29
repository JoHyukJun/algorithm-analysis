/*

    main.sql

    Created by JO HYUK JUN on 2023
    Copyright © 2023 JO HYUK JUN. All rights reserved.

*/


SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
    CASE
    WHEN (USED_GOODS_BOARD.STATUS = 'DONE') THEN '거래완료'
    WHEN (USED_GOODS_BOARD.STATUS = 'SALE') THEN '판매중'
    WHEN (USED_GOODS_BOARD.STATUS = 'RESERVED') THEN '예약중'
    END AS STATUS
FROM USED_GOODS_BOARD
WHERE DATE_FORMAT(CREATED_DATE, '%Y-%m-%d') = '2022-10-05'
ORDER BY BOARD_ID DESC