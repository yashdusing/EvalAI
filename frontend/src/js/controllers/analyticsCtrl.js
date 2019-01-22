// Invoking IIFE for dashboard
(function() {

    'use strict';

    angular
        .module('evalai')
        .controller('AnalyticsCtrl', AnalyticsCtrl);

    AnalyticsCtrl.$inject = ['utilities', '$state', '$rootScope'];

    function AnalyticsCtrl(utilities, $state, $rootScope) {
        var vm = this;

        vm.hostTeam = {};
        vm.teamId = null;
        vm.currentTeamName = null;
        vm.challengeListCount = 0;
        vm.challengeList = {};
        vm.challengeAnalysisDetail = {};
        vm.isTeamSelected = false;
        vm.challengeId = null;
        vm.currentChallengeDetails = {};
        vm.currentPhase = [];
        vm.totalSubmission = {};
        vm.totalParticipatedTeams = {};
        vm.lastSubmissionTime = {};

        var userKey = utilities.getData('userKey');

        var parameters = {};
        parameters.url = 'hosts/challenge_host_team/';
        parameters.method = 'GET';
        parameters.token = userKey;
        parameters.callback = {
            onSuccess: function(response) {
                var status = response.status;
                var details = response.data;
                if (status == 200) {
                    vm.hostTeam = details.results;

                }
            },
            onError: function(response) {
                var status = response.status;
                var error = response.data;
                if (status == 403) {
                    vm.error = error;

                    // navigate to permissions denied page
                    $state.go('web.permission-denied');
                }
            }
        };
        utilities.sendRequest(parameters);


        parameters.url = 'challenges/challenge?mode=host';
        parameters.method = 'GET';
        parameters.token = userKey;
        parameters.callback = {
            onSuccess: function(response) {
                var status = response.status;
                var details = response.data;
                if (status == 200) {
                    vm.challengeList = details.results;
                    vm.challengeListCount = details.count;
                }
            },
            onError: function(response) {
                var status = response.status;
                var error = response.data;
                if (status == 403) {
                    vm.error = error;

                    // navigate to permissions denied page
                    $state.go('web.permission-denied');
                }
            }
        };
        utilities.sendRequest(parameters);

        vm.showChallengeAnalysis = function() {
            if (vm.challengeId != null) {
                parameters.url = 'challenges/challenge/' + vm.challengeId + '/challenge_phase';
                parameters.method = 'GET';
                parameters.token = userKey;
                parameters.callback = {
                    onSuccess: function(response) {
                        var status = response.status;
                        var details = response.data;


                        if (status === 200) {
                            vm.currentPhase = details.results;
                            var challengePhaseId = [];
                            for (var phaseCount = 0; phaseCount < vm.currentPhase.length; phaseCount++) {
                                parameters.url = 'analytics/challenge/' + vm.challengeId + '/challenge_phase/' +  vm.currentPhase[phaseCount].id + '/analytics';
                                parameters.method = 'GET';
                                parameters.token = userKey;
                                challengePhaseId.push(vm.currentPhase[phaseCount].id);
                                parameters.callback = {
                                    onSuccess: function(response) {
                                        var status = response.status;
                                        var details = response.data;
                                        if (status == 200) {
                                            for(var i=0; i<challengePhaseId.length; i++) {
                                                if (challengePhaseId[i] == details.challenge_phase) {
                                                    vm.totalSubmission[challengePhaseId[i]] = details.total_submissions;
                                                    vm.totalParticipatedTeams[challengePhaseId[i]] = details.participant_team_count;
                                                    i++;
                                                    break;
                                                }
                                            }
                                        }
                                    },
                                    onError: function(response) {
                                        var status = response.status;
                                        var error = response.data;
                                        if (status == 403) {
                                            vm.error = error;

                                            // navigate to permissions denied page
                                            $state.go('web.permission-denied');
                                        } 
                                    }
                                };
                                utilities.sendRequest(parameters);
                            }

                            for (phaseCount = 0; phaseCount < vm.currentPhase.length; phaseCount++) {
                                parameters.url = 'analytics/challenge/' + vm.challengeId + '/challenge_phase/' +  vm.currentPhase[phaseCount].id + '/last_submission_datetime_analysis/';
                                parameters.method = 'GET';
                                parameters.token = userKey;
                                challengePhaseId.push(vm.currentPhase[phaseCount].id);
                                parameters.callback = {
                                    onSuccess: function(response) {
                                        var status = response.status;
                                        var details = response.data;
                                        if (status == 200) {
                                            for(var i=0; i<challengePhaseId.length; i++) {
                                                if (challengePhaseId[i] == response.data.challenge_phase) {
                                                    vm.lastSubmissionTime[challengePhaseId[i]] = details.last_submission_timestamp_in_challenge_phase;
                                                    i++;
                                                    break;
                                                }
                                            }
                                        }
                                    },
                                    onError: function(response) {
                                        var status = response.status;
                                        var error = response.data;
                                        if (status == 403) {
                                            vm.error = error;

                                            // navigate to permissions denied page
                                            $state.go('web.permission-denied');
                                        }
                                    }
                                };
                                utilities.sendRequest(parameters);
                            }

                        }
                    },
                    onError: function(response) {
                        var status = response.status;
                        var error = response.data;
                        if (status == 403) {
                            vm.error = error;

                            // navigate to permissions denied page
                            $state.go('web.permission-denied');
                        } 
                    }
                };

                utilities.sendRequest(parameters);
                vm.isTeamSelected = true;
                for (var i = 0; i < vm.challengeList.length; i++) {

                    if (vm.challengeList[i].id == vm.challengeId) {
                        vm.currentChallengeDetails = vm.challengeList[i];
                    }
                }
            } else {
                vm.isTeamSelected = false;
            }
        };
    }

})();
