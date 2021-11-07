

if __name__=="__main__":
        import service.generateRawInfo as generateRawInfo
        import configuration.config as config_interface
        import yinterface.yInterface as md_interface
        import marketApi.algoritms as algorithms_interface
        import utils.dumper as dumper

        value = generateRawInfo.GenerateRawInfo(config_interface, md_interface, algorithms_interface).do()
        dumper.dump(value, "d:\\tmp\\dumps")




        
