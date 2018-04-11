library(checkpoint)
checkpoint("2018-02-25", scanForPackages=F)

library(data.table)
library(ggplot2)


# Plot missing data points - Beijing
bj_aq <- rbindlist(lapply(Sys.glob("data/bj_*_renamed_aq.csv", dirmark = FALSE), fread))
bj_station <- fread("data/Beijing_AirQuality_Stations.csv")
# Dedup
bj_aq <- bj_aq[!duplicated(bj_aq, from_last=T)]
# Parse time
bj_aq[, time:=with_tz(ymd_hms(bj_aq[, time], tz="UTC"), tz="Asia/Shanghai")]
# Filling Gaps in Time
full_keys <- expand.grid(
    time=seq(ymd_hms("2017-01-01 16:00:00"), 
             ymd_hms("2018-03-30 16:00:00"), 
             by="1 hour"),
    station_id=unique(bj_aq[,station_id])
)
bj_aq_full <- merge(bj_aq, full_keys, by=c("time", "station_id"), all.y=T)
bj_aq_full[,PM25_NA := is.na(PM25_Concentration)]

plot_na <- ggplot(bj_aq_full[PM25_NA==1], 
                  aes(x=time, y=PM25_NA + runif(sum(bj_aq_full$PM25_NA==1), -0.1, 0.1))) +
    facet_wrap(~station_id, ncol=1) + geom_point(size=0.1, alpha=0.5) +
    labs(y="", title="Missing Data Points for Each Stations") +
    theme_bw() + theme(
        panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        axis.ticks.y=element_blank(),
        axis.text.y=element_blank()
    )
ggsave(filename="bj_na_plot.png", plot=plot_na, width=15, height=50, units="cm", scale=2, dpi=100)
plot_na <- ggplot(bj_aq_full, aes(x=time, y=PM25_NA + runif(nrow(bj_aq_full), -0.3, 0.3))) +
    facet_wrap(~station_id, ncol=1) + geom_point(size=0.1, alpha=0.5) +
    labs(y="", title="Missing Data for Each Stations (0: Exists, 1: Missing)") +
    theme_bw() + theme(
        panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank()      
    )
ggsave(filename="bj_na_plot_all.png", plot=plot_na, width=15, height=50, units="cm", scale=2, dpi=150)


# Plot missing data points - London
ld_aq <- rbindlist(lapply(Sys.glob("data/ld_*_renamed_aq.csv", dirmark = FALSE), fread))
ld_station <- fread("data/London_AirQuality_Stations.csv")
# Dedup
ld_aq <- ld_aq[!duplicated(ld_aq, from_last=T)]
# Parse time
ld_aq[, time:=ymd_hm(ld_aq[, time], tz="UTC")]
# Filling Gaps in Time
full_keys <- expand.grid(
    time=seq(ymd_hms("2017-01-02 00:00:00"), 
             ymd_hms("2018-03-30 00:00:00"), 
             by="1 hour"),
    station_id=unique(ld_aq[,station_id])
)
ld_aq_full <- merge(ld_aq, full_keys, by=c("time", "station_id"), all.y=T)
ld_aq_full[,PM25_NA := is.na(PM25_Concentration)]

plot_na <- ggplot(ld_aq_full[PM25_NA==1], 
                  aes(x=time, y=PM25_NA + runif(sum(ld_aq_full$PM25_NA==1), -0.1, 0.1))) +
    facet_wrap(~station_id, ncol=1) + geom_point(size=0.1, alpha=0.5) +
    labs(y="", title="Missing Data Points for Each Stations") +
    theme_bw() + theme(
        panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        axis.ticks.y=element_blank(),
        axis.text.y=element_blank()
    )
ggsave(filename="ld_na_plot.png", plot=plot_na, width=15, height=25, units="cm", scale=2, dpi=100)
plot_na <- ggplot(ld_aq_full, aes(x=time, y=PM25_NA + runif(nrow(ld_aq_full), -0.3, 0.3))) +
    facet_wrap(~station_id, ncol=1) + geom_point(size=0.1, alpha=0.5) +
    labs(y="", title="Missing Data for Each Stations (0: Exists, 1: Missing)") +
    theme_bw() + theme(
        panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank()
        # axis.ticks.y=element_blank(),
        # axis.text.y=element_blank()        
    )
ggsave(filename="ld_na_plot_all.png", plot=plot_na, width=15, height=25, units="cm", scale=2, dpi=150)
