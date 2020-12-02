-- CREATE LISTINGS_MAIN

CREATE TABLE public.listings_main_11282020
(
    main_id numeric,
    listing_id text,
    user_id text,
    title text,
    description text,
    price double precision,
    currency_code text,
    quantity numeric,
    url text,
    views numeric,
    num_favorers numeric,
    who_made text,
    when_made text,
    recipient text,
    occasion text,
    is_vintage text,
    PRIMARY KEY (main_id)
);

ALTER TABLE public.listings_main_11282020
    OWNER to postgres;

-- IMPORT LISTINGS_MAIN
\copy listings_main_11282020 (main_id,listing_id,user_id,title,description,price,currency_code,quantity,url,views,num_favorers,who_made,when_made,recipient,occasion,is_vintage) from '/Users/kristinafrazier/documents/projects/etsy/data/nov_2020/listings_main.csv' delimiter ',' csv header;
