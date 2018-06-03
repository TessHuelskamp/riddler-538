my_data <-read.csv("results.csv")
jpeg("graph.jpg")
matplot(my_data["NUM_HOUSES"], my_data["AVG"], type="l", xlim=c(0, max(my_data["NUM_HOUSES"])), ylim=c(0, max(my_data["AVG"])))
