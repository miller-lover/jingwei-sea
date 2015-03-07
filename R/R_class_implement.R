# R Class Implementation Example

setClass("TimeSeries",representation(data="numeric", start="POSIXct", end="POSIXct" ))

my.TimeSeries <- new("TimeSeries",
	data=c(1,2,3,4,5,6),
	start=as.POSIXct("07/01/2009 0:00:00",tz="GMT", format="%m/%d/%Y %H:%M:%S"),
	end=as.POSIXct("07/01/2009 0:05:00",tz="GMT", format="%m/%d/%Y %H:%M:%S")
)

setValidity("TimeSeries",
	function(object) {
		object@start <= object@end &&
		length(object@start) == 1 &&
		length(object@end) == 1
	}
)

validObject(my.TimeSeries)

period.TimeSeries <- function(object) {
	if (length(object@data) > 1) {
		(object@end - object@start) / (length(object@data) - 1)
	} else {
		Inf
	}
}

series <- function(object) {object@data}

setGeneric("series")

series(my.TimeSeries)

period <- function(object) {object@period}

setGeneric("period")

setMethod(period, signature=c("TimeSeries"), definition=period.TimeSeries)

showMethods("period")

period(my.TimeSeries)

setMethod("summary",
	signature="TimeSeries",
	definition=function(object) {
		print(paste(object@start," to ", object@end, sep="",collapse=""))
		print(paste(object@data,sep="",collapse=","))
	}
)

summary(my.TimeSeries)
# summary results
# [1] "2009-07-01 to 2009-07-01 00:05:00"
# [1] "1,2,3,4,5,6"

# You can even define a new method for an existing operator
setMethod("[",
	signature=c("TimeSeries"),
	definition=function(x, i, j, ...,drop) {
		x@data[i]
	}
)

# WeightHistory class based on the TimeSeries class.
setClass(
	"WeightHistory",
	representation(
		height = "numeric",
		name = "character"
	),
	contains = "TimeSeries"
)


# create a WeightHistory object, populating slots named in TimeSeries and the new slots for WeightHistory
john.doe <- new("WeightHistory",
	data=c(170, 169, 171, 168, 170, 169),
	start=as.POSIXct("02/14/2009 0:00:00",tz="GMT",	format="%m/%d/%Y %H:%M:%S"),
	end=as.POSIXct("03/28/2009 0:00:00",tz="GMT", format="%m/%d/%Y %H:%M:%S"),
	height=72,
	name="John Doe"
)

# created a Person class containing a person's name and height
setClass(
	"Person",
	representation(
		height = "numeric",
		name = "character"
	)
)

# Now, create an alternative weight history that inherits from both a TimeSeries object and a Person object
setClass(
	"AltWeightHistory",
	contains = c("TimeSeries", "Person")
)

# Suppose that we also had created a class to represent cats
setClass(
	"Cat",
	representation(
		breed = "character",
		name = "character"
	)
)

setClassUnion(
	"NamedThing",
	c("Person","Cat")
)

jane.doe <- new("AltWeightHistory",
	data=c(130, 129, 131, 128, 130, 129),
	start=as.POSIXct("02/14/2009 0:00:00",tz="GMT", format="%m/%d/%Y %H:%M:%S"),
	end=as.POSIXct("03/28/2009 0:00:00",tz="GMT", format="%m/%d/%Y %H:%M:%S"),
	height=67,
	name="Jane Doe"
)

is(jane.doe,"NamedThing")