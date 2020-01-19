data(mtcars)


# Testing difference in  means H0 = mu1 - mu2 = 0
# Z test from data
z.test(x = mtcars$mpg, y = mtcars$cyl, sigma.x = sd(mtcars$mpg), sigma.y = sd(mtcars$cyl))

# Z test from stats
zsum.test(mean.x = mean(mtcars$mpg), mean.y = mean(mtcars$cyl), n.x = length(mtcars$mpg), n.y = length(mtcars$cyl), sigma.x = sd(mtcars$mpg), sigma.y = sd(mtcars$cyl))

# t test from data
# compare variances first
t.test(x = mtcars$mpg, y = mtcars$cyl, var.equal = TRUE)

# t test from stats
tsum.test(mean.x = mean(mtcars$mpg), mean.y = mean(mtcars$cyl), s.x = sd(mtcars$mpg), s.y = sd(mtcars$cyl),  n.x = length(mtcars$mpg), n.y = length(mtcars$cyl), var.equal = TRUE)

# comparing two population proportions
prop.test(x = c(120, 140), n = c(300, 700), correct = FALSE)

# comparing variances
# F Test using data
var.test(x = mtcars$mpg, y = mtcars$cyl)


# F test using stats
FTest = var(mtcars$mpg)/var(mtcars$cyl)

2 * pf(FTest, df1 = length(mtcars$mpg)-1, df2 = length(mtcars$cyl)-1, lower.tail = FALSE)


# paired variance test
# test using data
t.test(x = mtcars$mpg, y = mtcars$cyl, paired = TRUE)

# test using data
tsum.test(mean.x = mean(mtcars$mpg), mean.y = mean(mtcars$cyl), s.x = sd(mtcars$mpg), s.y = sd(mtcars$cyl),  n.x = length(mtcars$mpg), n.y = length(mtcars$cyl))

# testing population proportion
prop.test(x = 8, n = 25)

# Variables are independent
test = chisq.test(mtcars$mpg, mtcars$cyl)


