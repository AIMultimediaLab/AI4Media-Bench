<management>
    <!--Todo: ultimately decide whether this belongs on tasks:management or dataset:management
            Is currently at both locations-->
    <div class="ui top attached tabular menu">
        <div class="active item" data-tab="submissions">Submissions</div>
        <div class="item" data-tab="datasets">Datasets and programs</div>
        <div class="item" data-tab="tasks">Tasks</div>
        <div class="right menu">
            <div class="item">
                <help_button href="https://github.com/AIMultimediaLab/AI4MediaBench-AIMultimediaLab/blob/main/Task-and-Dataset-Management.MD"
                             tooltip_position="left center">
                </help_button>
            </div>
        </div>
    </div>
    <div class="ui active bottom attached tab segment" data-tab="submissions">
        <submission-management></submission-management>
    </div>
    <div class="ui bottom attached tab segment" data-tab="datasets">
        <data-management></data-management>
    </div>
    <div class="ui bottom attached tab segment" data-tab="tasks">
        <task-management></task-management>
    </div>

    <script>
        let self = this

        self.on('mount', () => {
            $('.ui.menu .item', self.root).tab()
        })
    </script>

</management>