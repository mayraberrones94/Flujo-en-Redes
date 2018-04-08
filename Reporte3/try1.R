NoDirigido <- read.csv("TiempoNoDir.csv", header = FALSE)
Dirigido <- read.csv("TiempoDir.csv", header = FALSE)

TiempoNoDir <- data.frame()
for(i in 1:20){
	TiempoNoDir <- rbind(TiempoNoDir, NoDirigido[((10 * i) - 9): (10 *i),])
}
print(shapiro.test(TiempoNoDir[,1]))

pdf("TiempoNoDirFinal.pdf")
boxplot(t(TiempoNoDir), xaxt = "n", ylim = c(0,3), xlab = c("Cantidad de nodos"), ylab = c("Tiempo en segundos"))
axis(1, at = 1:20, labels = seq(5, 100, 5))
par(new = TRUE)
plot(exp, xlab = "", ylab = "", col = "blue", lwd = 3, xaxt = "n", ylim = c(1, 3))

TiempoDir <- data.frame()
for(i in 1:20){
	TiempoDir <- rbind(TiempoDir, Dirigido[((10 * i) - 9): (10 *i),])
}
print(shapiro.test(TiempoDir[,1]))

pdf("TiempoDirFinal.pdf")
boxplot(t(TiempoDir), xaxt = "n", ylim = c(0,3), xlab = c("Cantidad de nodos"), ylab = c("Tiempo en segundos"))
axis(1, at = 1:20, labels = seq(5, 100, 5))
par(new = TRUE)
plot(exp, xlab = "", ylab = "", col = "blue", lwd = 3, xaxt = "n", ylim = c(1, 3))
graphics.off()
