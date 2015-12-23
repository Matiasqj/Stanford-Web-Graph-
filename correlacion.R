lectura1 = read.table(file.choose())
dirigido = matrix(lectura1$V2, byrow = TRUE, ncol = 1)
lectura2 = read.table(file.choose())
nodirigido = matrix(lectura2$V2, byrow = TRUE, ncol = 1)

cor(dirigido, nodirigido, method = "spearman")
cor(dirigido, nodirigido, method = "kendal")
plot(dirigido, nodirigido, xlab="dirigidos", ylab="no dirigidos", pch=1, col="blue" )