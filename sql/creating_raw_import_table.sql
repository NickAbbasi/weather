create table weather_data.raw_import_hourly(
station varchar(255),
date datetime,
lon varchar(255),
lat varchar(255),
tmpfv decimal (8,4),
dwpf decimal (8,4),
relh decimal (8,4),
drct	decimal (10,4),
sknt	decimal (8,4),
p01i	decimal (8,4),
alti	decimal (8,4),
mslp	decimal (10,4),
vsby	decimal (8,4),
gust	decimal (8,4),
skyc1	varchar(255),
skyc2	varchar(255),
skyc3	varchar(255),
skyc4	varchar(255),
skyl1	decimal (12,4),
skyl2	decimal (12,4),
skyl3	decimal (12,4),
skyl4	decimal (12,4),
wxcodes	varchar(255),
ice_accretion_1hr	varchar(255),
ice_accretion_3hr	varchar(255),
ice_accretion_6hr	varchar(255),
peak_wind_gust	decimal (12,4),
peak_wind_drct	varchar(255),
peak_wind_time	time,
feel	 decimal (8,4),
metar text



) 