<submission-limit>
  <div class="ui sixteen wide column submission-container">
    <div class="col">
        <div class="col-content">
            Number of submissions used for the day
        </div>
        <span show="{selected_phase.max_submissions_per_day > 0 && selected_phase.max_submissions_per_person > 0}" class="badge {badgeColor(selected_phase.used_submissions_per_day, selected_phase.max_submissions_per_day)}">
            {selected_phase.used_submissions_per_day} out of {selected_phase.max_submissions_per_day}
        </span>
    </div>
    <div class="col">
        <div class="col-content">
            Number of total submissions used
        </div>
        <span show="{selected_phase.max_submissions_per_person > 0 && selected_phase.max_submissions_per_day > 0}" class="badge {badgeColor(selected_phase.used_submissions_per_person, selected_phase.max_submissions_per_person)}">
            {selected_phase.used_submissions_per_person} out of {selected_phase.max_submissions_per_person}
        </span>
    </div>
  </div>

  <script>
    this.selected_phase = {};

    this.badgeColor = function(used, max) {
      // Calculate the percentage of used submissions
      var percentage = (used / max) * 100;

      // Determine the badge color based on the percentage
      if (percentage < 5) {
        return "badge-green";
      } else if (percentage < 25) {
        return "badge-yellow";
      } else if (percentage >= 25 && percentage < 50) {
        return "badge-orange";
      } else if (percentage >= 50 && percentage < 75) {
        return "badge-pink";
      } else {
        return "badge-red";
      }
    };

    this.on('mount', function () {
      CODALAB.events.on('phase_selected', (selected_phase) => {
        this.selected_phase = selected_phase;
        this.update();
      });
    });
  </script>

    <style type="text/stylus">
        .submission-container
            margin-top 1em
            background-color white
            padding 2em
            border solid 1px #dcdcdcdc
            display flex

        .col
            flex 1
            display flex
            flex-direction column
            justify-content space-between

        .col-content
            font-weight bold
            text-align center

        .badge
            padding 0.5em 1em
            text-align center
            display inline-block
            width max-content
            margin 0 auto
            margin-top 0.5em
            border-radius 5px

        .badge-green
            background-color #a5d6a7

        .badge-yellow
            background-color #fff59d

        .badge-orange
            background-color #ffcc80

        .badge-pink
            background-color #ff80ab

        .badge-red
            background-color #e57373


    </style>
</submission-limit>
