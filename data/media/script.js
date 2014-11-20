function DropDown1(type) {
	localStorage.BrightnessController_type1 = type
	updateTitle1(localStorage.BrightnessController_brightness1)
}

function DropDown2(type) {
	localStorage.BrightnessController_type2 = type
	updateTitle2(localStorage.BrightnessController_brightness2)
}

function updateTitle1(val) {
	document.title = "xrandr --output " + localStorage.BrightnessController_type1 + " --brightness " + val
	localStorage.BrightnessController_brightness1 = val
	$("#slider1value").html(Math.round(val * 100))
}

function updateTitle2(val) {
	document.title = "xrandr --output " + localStorage.BrightnessController_type2 + " --brightness " + val
	localStorage.BrightnessController_brightness2 = val
	$("#slider2value").html(Math.round(val * 100))
}

function MasterControl() {
	var number = $('input[name=number]').val()
	var type = $('input[name=type]').val()
	var value = $('input[name=value]').val()
	document.title = "xrandr --output " + type + number + " --brightness " + (value / 100)
}

$(document).ready(function () {
	//On first run, brightness will be 1
	if (localStorage.getItem("BrightnessController_brightness1") === null) {
		localStorage.BrightnessController_brightness1 = 1
		localStorage.BrightnessController_brightness2 = 1
		localStorage.BrightnessController_type1 = "VGA1"
		localStorage.BrightnessController_type2 = "VGA2"
	}
	$("#slider1 input[type=range]").val(localStorage.BrightnessController_brightness1)
	$("#slider2 input[type=range]").val(localStorage.BrightnessController_brightness2)
	$("#slider1 select").val(localStorage.BrightnessController_type1)
	$("#slider2 select").val(localStorage.BrightnessController_type2)
	updateTitle1(localStorage.BrightnessController_brightness1)
	updateTitle2(localStorage.BrightnessController_brightness2)
});

$("input, select, .close, .minimize").mouseover(function () {
	document.title = "disable_drag"
}).mouseout(function () {
	document.title = "enable_drag"
}).click(function () {
	if ($(this).hasClass("close")) {
		document.title = "close"
	} else if ($(this).hasClass("minimize")) {
		document.title = "minimize"
	}
})