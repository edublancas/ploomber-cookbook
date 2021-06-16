from ploomber import OnlineDAG


class MyModel:
    def predict(self, number):
        return number + 1


class InferencePipeline(OnlineDAG):
    @staticmethod
    def get_partial():
        # the current API requires a yaml file but for your use case,
        # it makes more sense to pass the list of functions to use directly
        # I can work on updating that
        return 'tasks.yaml'

    @staticmethod
    def terminal_params():
        # these are the params required for the terminal task (the last
        # function to execute. Since loading a model into memory takes
        # time, we load it here and re-use it for future inferences
        return dict(model=MyModel())

    @staticmethod
    def terminal_task(upstream, model):
        return model.predict(upstream['combine'])


# when creating the pipeline, ploomber figures out dependencies by looking
# at references in the code (see tasks.py for details) and routes each output
# to the function that requires it
inference = InferencePipeline()

# this returns the output of all tasks, useful for debugging
out = inference.predict(get=[1, 1])

print(out)
