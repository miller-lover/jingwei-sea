#!/usr/bin/perl
# file to preprocess (and filter) mortality data

	print "ResidentStatus,Education1989,Education2003,EducationFlag," .
	"MonthOfDeath,Sex,AgeDetail,AgeSubstitution,AgeRecode52," .
	"AgeRecode27,AgeRecode12,AgeRecodeInfant22,PlaceOfDeath," .
	"MaritalStatus,DayOfWeekofDeath,CurrentDataYear,InjuryAtWork," .
	"MannerOfDeath,MethodOfDisposition,Autopsy,ActivityCode," .
	"PlaceOfInjury,ICDCode,CauseRecode358,CauseRecode113," .
	"CauseRecode130,CauseRecord39,Race,BridgeRaceFlag," .
	"RaceImputationFlag,RaceRecode3,RaceRecord5,HispanicOrigin," .
	"HispanicOriginRecode\n";
	
while(<>) {
	my ($X0,$ResidentStatus,$X1,$Education1989,$Education2003,
	$EducationFlag,$MonthOfDeath,$X5,$Sex,$AgeDetail,
	$AgeSubstitution,$AgeRecode52,$AgeRecode27,$AgeRecode12,
	$AgeRecodeInfant22,$PlaceOfDeath,$MaritalStatus,
	$DayOfWeekofDeath,$X15,$CurrentDataYear,$InjuryAtWork,
	$MannerOfDeath,$MethodOfDisposition,$Autopsy,$X20,$ActivityCode,
	$PlaceOfInjury,$ICDCode,$CauseRecode358,$X24,$CauseRecode113,
	$CauseRecode130,$CauseRecord39,$X27,$Race,$BridgeRaceFlag,
	$RaceImputationFlag,$RaceRecode3,$RaceRecord5,$X32,
	$HispanicOrigin,$X33,$HispanicOriginRecode,$X34)
	
	= unpack("a19a1a40a2a1a1a2a2a1a4a1a2a2a2a2a1a1a1a16a4a1" .
	"a1a1a1a34a1a1a4a3a1a3a3a2a283a2a1a1a1a1a33a3a1a1",
	$_);


	print "$ResidentStatus,$Education1989,$Education2003,".
	"$EducationFlag,$MonthOfDeath,$Sex,$AgeDetail,".
	"$AgeSubstitution,$AgeRecode52,$AgeRecode27,".
	"$AgeRecode12,$AgeRecodeInfant22,$PlaceOfDeath," .
	"$MaritalStatus,$DayOfWeekofDeath,$CurrentDataYear,".
	"$InjuryAtWork,$MannerOfDeath,$MethodOfDisposition,".
	"$Autopsy,$ActivityCode,$PlaceOfInjury,$ICDCode,".
	"$CauseRecode358,$CauseRecode113,$CauseRecode130,".
	"$CauseRecord39,$Race,$BridgeRaceFlag,$RaceImputationFlag,".
	"$RaceRecode3,$RaceRecord5,$HispanicOrigin," .
	"$HispanicOriginRecode\n";
}

# I executed this script with the following command in a bash shell:
# ./mortalities.pl < MORT06.DUSMCPUB > MORT06.csv