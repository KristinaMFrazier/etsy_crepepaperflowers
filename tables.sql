-- Table creation and import codes for data uploads

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
    is_vintage text
);

ALTER TABLE public.listings_main_11282020
    OWNER to postgres;

-- IMPORT LISTINGS_MAIN
\copy listings_main_11282020 (main_id,listing_id,user_id,title,description,price,currency_code,quantity,url,views,num_favorers,who_made,when_made,recipient,occasion,is_vintage) from '/Users/kristinafrazier/documents/projects/etsy/data/nov_2020/listings_main.csv' delimiter ',' csv header;

--------------------------------------------------------------------------------

-- CREATE LISTINGS_TAGS

CREATE TABLE public.listings_tags_11282020
(
    main_id numeric,
    tags text
);

ALTER TABLE public.listings_tags_11282020
    OWNER to postgres;


-- IMPORT LISTINGS_TAGS
\copy listings_tags_11282020 (main_id,tags) from '/Users/kristinafrazier/documents/projects/etsy/data/nov_2020/listings_tags.csv' delimiter ',' csv header;

--------------------------------------------------------------------------------

-- CREATE LISTINGS_MATERIALS

CREATE TABLE public.listings_materials_11282020
(
    main_id numeric,
    materials text
);

ALTER TABLE public.listings_materials_11282020
    OWNER to postgres;


-- IMPORT LISTINGS_MATERIALS
\copy listings_materials_11282020 (main_id,materials) from '/Users/kristinafrazier/documents/projects/etsy/data/nov_2020/listings_materials.csv' delimiter ',' csv header;

--------------------------------------------------------------------------------

-- CREATE LISTINGS_STYLE

CREATE TABLE public.listings_style_11282020
(
    main_id numeric,
    style text
);

ALTER TABLE public.listings_style_11282020
    OWNER to postgres;


-- IMPORT LISTINGS_STYLE
\copy listings_style_11282020 (main_id,style) from '/Users/kristinafrazier/documents/projects/etsy/data/nov_2020/listings_style.csv' delimiter ',' csv header;

--------------------------------------------------------------------------------

-- CREATE LISTINGS_TAXONOMY

CREATE TABLE public.listings_taxonomy_11282020
(
    main_id numeric,
    taxonomy_path text
);

ALTER TABLE public.listings_taxonomy_11282020
    OWNER to postgres;


-- IMPORT LISTINGS_TAXONOMY
\copy listings_taxonomy_11282020 (main_id,taxonomy_path) from '/Users/kristinafrazier/documents/projects/etsy/data/nov_2020/listings_taxonomy.csv' delimiter ',' csv header;
